from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def welcome(request):
    details_url = reverse('teachers:teacher_details')
    response = f'<h1><a href="{details_url}"> Welcome teachers </a></h1>'
    return HttpResponse(response)

def bye(request):
    return HttpResponse('<h1>Goodbye teachers</h1>')


def teacher_details(request):
    details = """
    <h1> Teacher details </h1>
    <ul>
        <li> Name: Dr. Sharanya </li>
        <li> Subject: Cloud AWS </li>
        <li> Teacher ID: DCI123 </li>
    </ul>
    """
    return HttpResponse(details)