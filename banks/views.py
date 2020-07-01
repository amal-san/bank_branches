from django.shortcuts import render ,redirect
from .serializers import *
from .models import *
from rest_framework import generics
from django.views import View
from rest_framework.response import Response
from django.db.models import Q
from django.http import HttpResponse


class Home(View):

    def get(self,request):
        return render(request,'index.htm')

    def get_form(self,request):
        try:
            form = request.POST['form1']
        except:
            form = request.POST['form2']
        finally:
            return form
        
    
    def post(self,request):
        if request.method == "POST":

            form = self.get_form(request)
            print(form)
            
            if (form == '1'):
                ifsc = request.POST['ifsc']
                print(ifsc)
                if " " not in ifsc and not None:
                    return redirect('branch_ifsc/'+ ifsc)
                else:
                    return render(request,'index.htm',{"error_form1":"Enter correct IFSC code !"})
            elif (form == '2'):
                name = request.POST['name']
                city = request.POST['city']
                if name is not '' and city is not '':
                    return redirect('branches/'+ name + '/'+ city)
                else:
                    return render(request,'index.htm',{"error_form2":"Enter in both field !"})
            
            else:
                return render(request,'index.htm',{"global":"Don't search on both forms"})

            

    

class BanksView(generics.ListCreateAPIView):
	queryset = Banks.objects.all()
	serializer_class = BanksSerializer


class BranchesIfscView(generics.ListCreateAPIView):

    """
    
    Return Branch details giving IFSC code query.

    """
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer


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