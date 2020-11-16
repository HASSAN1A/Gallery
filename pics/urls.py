
from django.conf.urls import url 
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$', views.welcome, name = 'welcome'),  #url to direct to the home page
    url('^today/$', views.todays_pics, name = 'todaysPics'),  #url to direct to pictures posted today.
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_pics, name = 'pastPics'),  #url to direct to pictures posted in the past.
    url(r'^search/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

