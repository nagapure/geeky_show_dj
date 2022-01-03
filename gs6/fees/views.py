from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fees_django(request):
    return HttpResponse(" Django fee is 500!")


def fees_python(request):
    return HttpResponse(" Python fee is 300!")