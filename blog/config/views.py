from pydoc_data.topics import topics
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Entry, Topic


def home(request):
    latest_entries_list = Entry.objects.order_by('-pub_date')[:6]
    latest_topics_list = Topic.objects.all()
    context = {
        'latest_entry_list' : latest_entries_list,
        'latest_topics_list' : latest_topics_list,
        
        }
    return render(request, 'config/index.html', context)

def entries(request, id):
    latest_entries_list = Entry.objects.filter(topics=id)
    data = {'response' : latest_entries_list}
    return JsonResponse(data)



def entry_detail(request, entry_id):
    return HttpResponse("Entry detail page" +str(entry_id))