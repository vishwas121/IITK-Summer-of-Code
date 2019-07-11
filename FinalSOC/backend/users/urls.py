from django.conf.urls import include, url
from .views import CirculationView

urlpatterns = [
    url(r'^$',CirculationView.as_view({'get':'list',"post":'create'}))
]
