from django.urls import include, path
from .views import *

urlpatterns = [
    path('banks/',BanksView.as_view()),
    path('branch_ifsc/<slug:ifsc>/', BranchesIfscView.as_view()),
    path('branches/<str:name>/<str:city>/', AllBranchesView.as_view())
    
]

