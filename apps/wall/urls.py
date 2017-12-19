from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.index, name="dashboard"),
    # url(r'^personal$', views.personal, name="personal"),
    url(r'^quotes$', views.quotes, name="quotes"),    

]
