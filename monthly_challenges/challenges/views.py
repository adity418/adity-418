from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    if month == "january":
        challenge_text = "This works"
    elif month == "february":
        challenge_text = "Walk for atleast 20 min"
    elif month == "march":
        challenge_text = "learn django every day 1 hour"
    elif month == "april":
        challenge_text = "learn python every day 1 hour"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)