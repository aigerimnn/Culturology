from django.urls import path
from .views import PeopleListCreateView, PeopleDetailView

urlpatterns = [
    path('peoples/', PeopleListCreateView.as_view(), name='people-list'),
    path('peoples/<int:pk>/', PeopleDetailView.as_view(), name='people-detail'),
]
