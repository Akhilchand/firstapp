# from django.conf.urls import include, url
# from django.contrib import admin

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'firstappproject.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# ]
from django.contrib import admin
#from django.urls import include, path
from django.conf.urls import patterns,url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^app/', include('app.urls', namespace = "app")),
]	
