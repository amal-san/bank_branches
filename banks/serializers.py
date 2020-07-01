from rest_framework import serializers

from .models import *

class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = "__all__"

class BranchesSerializer(serializers.ModelSerializer):
    bank_name = serializers.SerializerMethodField('get_bank_name')

    class Meta:
        model = Branches
        fields = (
        "bank_name",
        "ifsc",
        "branch",
        "address",
        "city",
        "district",
        "state",
       
        )

    def get_bank_name(self,obj):
        bank_name = Banks.objects.filter(name = obj.bank).values('name')
        return bank_name