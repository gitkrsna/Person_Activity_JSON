from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()