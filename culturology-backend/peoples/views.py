from rest_framework import generics
from .models import People
from .serializers import PeopleSerializer

class PeopleListCreateView(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

class PeopleDetailView(generics.RetrieveAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
