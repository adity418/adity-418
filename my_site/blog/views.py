from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create yottpResponse()ur views here.
def starting_page(request):
    return render(request, "blog/startingpage.html")

def posts(request):
    pass

def post_details(request):
    pass