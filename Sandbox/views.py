from wsgiref import headers
from django.http import (HttpResponse, HttpRequest, HttpResponseBadRequest, 
    HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect, 
    HttpResponseServerError, JsonResponse)
from django.shortcuts import HttpResponsePermanentRedirect, render
from django.core.serializers.json import DjangoJSONEncoder

#Установка и запрос куки:

def set(request):
    username = request.GET.get("username", "Undefined")
    response = HttpResponse(f"Salam {username}")
    response.set_cookie("username", username)
    return response

def get(request):
    username = request.COOKIES["username"] #незашифрованы
    return HttpResponse(f"Hello {username}")

#Отправка в формате JSON
def data(request):
    bob = Person("hui", 3)
    return JsonResponse(bob, safe = False, encoder = PersonEncoder)

class Person:
    def __init__(self, name = "Undefided", age = 0) -> None:
        self.name = name
        self.age = age
class PersonEncoder(DjangoJSONEncoder): #класс кодировщика
    def default(self,obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
            # return obj.__dict__
        return super().default(obj)
#Проверка введенных данных и обработка запросов (ошибки)
def index(request, id): #запрос id в адрессной строке
   people = ["Tom", "Bob", "Sam"] #массив
   if id in range(0, len(people)): #сравнение значения id с длинной массива
    return HttpResponse(people[id]) 
   else:
    return HttpResponseNotFound("not found")

def access (requst, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("не верные данные")
    if (age > 17):
        return HttpResponse("Заходи")
    else:
        return HttpResponseForbidden("Пиздуй отсюда")
def shit(request):
    return HttpResponseServerError("Сервер R.I.P")
#Запрос с определенными параметрами
def about(request, name = "Undefinded", size = 0 ):
    return HttpResponse(f"""<h2>Info</h2>
    <p>Name: {name}</p>
    <p>Size: {size}</p>""")

#параметры строки запроса ? и &
def contact(request): 
    work = request.GET.get("work", "Undefined")
    workplace = request.GET.get("workplace", "Undefined")
    return HttpResponse(f"<h2>Работа: {work} Место: {workplace}</h2>", headers={"secret_code": "1488"})# ответ на запрос с определением атрибута

# запросы из группы - contact_patterns
def vlozh(request, id):
    HttpResponse(f"Элемент: {id}")
def work(request, id):
    return HttpResponse(f"work: {id}") 
def workplace(request, id):
    return HttpResponse(f"workplace: {id}")  

def main(request):
    return HttpResponse("""<H2>Главная</H2>
    <p>проект на джанго развернутый локально и выброшенный в интернеты</p>""")
#редирект временный и постоянный
def options(request):
    header = ("Данные субъекта")
    langs = ["python", "c#", "basic"] #список
    bio = {"name": "Pukich", "age": "54"} #словарь
    adress = ("Петровско-Разумовская", 185, 10) #кортеж

    
    data = {"header": header, "langs": langs, "bio": bio, "adress": adress, "person": Person("Tom")}  #Данные для шаблона HTML(в кавычках обращение к переменной внутри html)
    return render(request, "example_site.html", context=data)
    
def setting(request):
    data1 = {"x": 5}
    return render(request, "site2.html", context=data1)

def cicles(request):
    cats = ["murzik", "vasya", "kitty", "murka"]
    return render(request, "site2.html", context={"cats": cats})

    