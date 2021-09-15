from typing import AsyncGenerator
from django.shortcuts import render

# Create your views here.
import json

from django.http    import JsonResponse
from django.views   import View

from dogs.models import Owners, Dogs

class OwnersView(View):
    def post(self, request):
        data   = json.loads(request.body)
        owners = Owners.objects.create(
            name    = data['owners'],
            email   = data['email'],
            age     = data['age']
            )
        dogs   = Dogs.objects.create(
            
        )