from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

challenges_month = {
    "january": "Learn Angular",
    "feburary": "Learn Reactjs",
    "march": "Learn Postgresql",
    "april": "Learn Python",
    "may": "Learn DSAL",
    "june": "Learn Django",
    "july": None,
    "August": None,
    "Septemeber": None,
    "October": None,
    "November": None,
    "December": None
}


# def jan(request):
#     return HttpResponse("Eat no meat for a month")


# def feb(request):
#     return HttpResponse("Walk for 20 minutes")

# dynamic response


# def Monthly_Challenges(request, month):
#     text = None
#     if month == "jan":
#         text = "Eat no meat for a month"
#     elif month == "feb":
#         text = "Walk for 20 minutes atleast"
#     else:
#         HttpResponseNotFound("this month not schedule yet")

#     return HttpResponse(text)


def index(request):
    items = ""
    month_keys = list(challenges_month.keys())
    return render(request, "challenges/index.html", {"months": month_keys})
    # for month in month_keys:
    #     redirect_url = reverse('month-challenge', args=[month])
    #     items += f"<li><a href={redirect_url}> {month} </a></li>"
    # content = f"<ul>{items}</ul>"
    # return HttpResponse(content)


def Monthly_Challenge_By_Number(request, month):
    keys = list(challenges_month.keys())
    fetch_idx = keys[month-1]
    if month > len(keys):
        return HttpResponseNotFound("invalid month")

    redirect_path = reverse("month-challenge", args=[fetch_idx])
    # return HttpResponseRedirect("/challenges/" + str(fetch_idx))
    text = f"<h1>hello user nice to meet you whats goin on</h1>"
    return HttpResponseRedirect(redirect_path)


def Monthly_Challenges(request, month):
    try:
        rendering_template = render_to_string("challenges/challenge.html")
        # return HttpResponse(challenges_month[month])
        # return HttpResponse(rendering_template)
        mnth = challenges_month[month]
        return render(request, 'challenges/challenge.html', {"text": mnth, "title": month.capitalize()})
    except:
        # return HttpResponseNotFound("this month not yet schedule")
        raise Http404()
