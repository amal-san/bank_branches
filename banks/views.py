from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from django.views import View
from rest_framework.response import Response
from django.db.models import Q
from django.http import HttpResponse






class BanksView(generics.ListCreateAPIView):
	queryset = Banks.objects.all()
	serializer_class = BanksSerializer


class BranchesIfscView(generics.ListCreateAPIView):

    """
    
    Return Branch details giving IFSC code query.

    """
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer


    def post(self, request, format=None):
        return {"ifsc":"asdfasdf"}


    def get_queryset(self):
        print(type(self.kwargs['ifsc']))
        return Branches.objects.filter(ifsc=self.kwargs['ifsc'])
    
    def get_branches_ifsc(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = BranchesSerializer(queryset, many=True)
        return Response(serializer.data)
	

class AllBranchesView(generics.ListCreateAPIView):

    """
    
    Return all Branches details giving city and name as query.

    """
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer


    def get_queryset(self):
        print(self.kwargs['name'])
        print(self.kwargs['city'])
        return Branches.objects.filter(Q(bank__name=self.kwargs['name'])  &  Q(city=self.kwargs['city']))
    
    def get_branches_ifsc(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = BranchesSerializer(queryset, many=True)
        return Response(serializer.data)