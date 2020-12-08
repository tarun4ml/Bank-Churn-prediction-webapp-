from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('myAPI', views.ExitedView)
urlpatterns = [
    path('', views.cxcontact, name='home'),
    path('about/', views.about, name='about'),

]