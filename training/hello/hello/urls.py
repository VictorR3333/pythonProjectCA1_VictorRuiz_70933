from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

#Here we can see the different urls that are created to be able to go to the different views of the web.
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="polls/index.html"), name="home"),
]