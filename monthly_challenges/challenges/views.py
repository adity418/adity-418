from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
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
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ol>{list_items}</ol>"
    return HttpResponse(response_data)

def monthly_challenge_in_num(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge" , args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported")
    