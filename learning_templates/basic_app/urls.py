from django.urls import path
from django.conf.urls import url, include
from basic_app import views

#TEMPLATE TAGGING ---> django automatically looks for it
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
