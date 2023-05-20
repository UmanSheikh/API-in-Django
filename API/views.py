from django.shortcuts import HttpResponse
import pickle
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

@csrf_exempt
def results(request):
    if request.method == 'POST':
        path = os.path.join("static", "model")
        with open(path, 'rb') as f:
            model = pickle.load(f)
        
        data = JSONParser().parse(request)
        prediction = model.predict([[data["year"]]])
        print(data["dummy"])

    return JsonResponse({
        'prediction': prediction[0],
        'User': data["dummy"]
        })

@csrf_exempt
def deep_learning(request):
    return JsonResponse({"API":"Working"})