from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image

# Create your views here.

#Function to display the welcome page
def welcome (request):
    return render ( request, 'welcome.html')


#Function to display photos that have been posted today.
def todays_pics(request): 
    date = dt.date.today()
    pics = Image.todays_pics()

    return render (request, 'all-photos/recent_pics.html',{"date":date, "pics":pics})  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

#Function to redirect to photos posted in the past
def past_pics (request, past_date):
    #Convert date from the url string
    
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False
    
    if date ==dt.date.today():
        return redirect(todays_pics)

    return render(request, 'all-photos/past_pics.html', {"date": date})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images_by_category = Image.search_by_category(search_term)
        searched_images_by_location = Image.search_by_location(search_term)
        results = [*searched_images_by_category, *searched_images_by_location]
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": results})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
    
def image(request,category_id):
    try:
        image = Image.objects.get(id = category_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/images.html", {"image":image})







