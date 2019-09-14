# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#from django.template import loader, RequestContext
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question


def index(request):
	latest_questions = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('app/index.html')
	#context = RequestContext(request, {
	#	'latest_questions':latest_questions
	context = {'latest_questions':latest_questions}
	return render(request, 'app/index.html', context)

	#})
	#return HttpResponse(template.render(context))

def detail(request, question_id):
	#return HttpResponse("This is the detail view of the question: %s" % question_id)
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'app/detail.html', {'question' : question})

def results(request, question_id):
	#return HttpResponse("These are the results of the question: %s" % question_id)
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'app/results.html', {'question' : question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except:
		return render(request, 'app/detail.html', {'question': question, 'error_message':"Please select a choice"})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		return HttpResponseRedirect(reverse('app:results', args = (question_id,)))