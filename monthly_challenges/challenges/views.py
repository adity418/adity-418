from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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
    month_name = None
    if month == 1:
        month_name = 'january'
    elif month == 2:
        month_name = 'Feburary'
    elif month == 3:
        month_name = 'March'
    elif month == 4:
        month_name = 'April'
    elif month == 5:
        month_name = 'May'
    else:
        return HttpResponseNotFound("You have enter wrong number")
    return HttpResponse(month_name)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challen[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
    