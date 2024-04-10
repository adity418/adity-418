from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create yottpResponse()ur views here.
def starting_page(request):
    return render(request, "blog/startingpage.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post_details(request):
    pass 