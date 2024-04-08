from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challen = {
    "january": "Drink 8 glass of water daily",
    "february": "brush a teeth twice a day",
    "march": "Eat breakfast every mourning",
    "april": "Walk for atleast 20 min",
    "may": "Do brain training exercise",
    "june": "Sleep for 8-9 hours every night.",
    "july": "go to gym",
    "august": "Wake up early",
    "september": "Spend atleast 20 min in nature",
    "october": "read 20 pages daily",
    "november": "learn to write a python program daily",
    "december": "Write down a goal and look to achive it",
}

# Create your views here.
def monthly_challenge_in_num(request, month):
    months = list(monthly_challen.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge" , args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challen[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported")
    