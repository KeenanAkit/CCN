from django.urls import path
from . import views

urlpatterns = [
    path('api/ccna/', views.CcnaListCreate.as_view() ),
]
