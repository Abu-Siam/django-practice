from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import  render
from .models import Status

# Create your views here.
def home_view(request,*args,**kwargs):
    # return HttpResponse('<h1>Home</h1>')
    return render(request, 'pages/home.html',context={},status=200)
def status_list_view(request,*args,**kwargs):
    obj = Status.objects.all()
    status_list = [{"id": x.id,"content":x.content} for x in obj]
    data = {
        "response": status_list
    }
    return JsonResponse(data)
def detailed_status(request,status_id,*args,**kwargs):
    # try:
    #     obj = Status.objects.get(id=status_id)
    # except:
    #
    #     raise Http404
    data = {
        "id": status_id,

        # "content": obj.content,
        # "image": obj.image.url
    }
    try:
        obj = Status.objects.get(id=status_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status =  404
        # raise Http404

    return JsonResponse(data,status=status)
    # return HttpResponse(f'<h1>Detailed Status For { status_id }</h1>')