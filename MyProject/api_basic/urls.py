from django.urls import path
from . import views
from .views import articleListClass, articleDetailClass

urlpatterns = [
    path('article/', articleListClass.as_view() ),
    path('detail/<int:pk>/', articleDetailClass.as_view() )
    
]