from wsgiref import headers
from django.http import (HttpResponse, HttpRequest, HttpResponseBadRequest, 
    HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect, 
    HttpResponseServerError, JsonResponse)
from django.shortcuts import HttpResponsePermanentRedirect, render
from django.core.serializers.json import DjangoJSONEncoder




def auth(request):
    return render(request, "auth.html")

def postuser(request): #получение данных из формы запроса
    nomen = request.POST.get("nomen", "Undefined")
    cognomen = request.POST.get("cognomen", "Undefined")
    langs = request.POST.getlist("languages", ["python"])
     
    return HttpResponse(f"""
                <div>Name: {nomen}  Age: {cognomen}<div>
                <div>Languages: {langs}</div>
            """)

