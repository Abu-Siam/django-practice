import io

from django.contrib.auth.models import Permission
from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view, authentication_classes

from .models import Student
from .serializers import StudentSerializer,StudentModelSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .forms import StudentForm
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST','PUT','DELETE','PATCH'])
def student_view(request,id = None):
    if request.method == 'GET':
        # json_data = request.body
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser().parse(stream)
        # id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stud = Student.objects.all()
        serialized = StudentSerializer(stud,many=True)
        json_data = JSONRenderer().render(serialized.data)
        # return JsonResponse(serialized.data,safe=False)
        return Response(json_data)
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serialzer = StudentSerializer(data =python_data)
        if serialzer.is_valid():
            serialzer.save()
            msg = {'msg':'Data Created'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serialzer.errors)
        return HttpResponse(json_data, content_type='application/json')
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        # id = python_data.get('id',None)
        # if id is not None :
        stud = Student.objects.get(id=id)
        serialzer = StudentSerializer(stud,data =python_data, partial=True)
        if serialzer.is_valid():
            serialzer.save()
            msg = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serialzer.errors)
        return HttpResponse(json_data, content_type='application/json')
    if request.method == 'DELETE':
        stud = Student.objects.get(id=id)
        stud.delete()
        msg = {'msg': str(id) +'id Deleted'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')

@method_decorator(csrf_exempt,name='dispatch')
class StudentApi(View):
    def get(self, request,id=None,  *args,**kwargs):
        if request.method == 'GET':
            # json_data = request.body
            # stream = io.BytesIO(json_data)
            # python_data = JSONParser().parse(stream)
            # id = python_data.get('id',None)
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            stud = Student.objects.all()
            serialized = StudentSerializer(stud, many=True)
            # json_data = JSONRenderer().render(serialized.data)
            return JsonResponse(serialized.data, safe=False)

    def post(self, request,*args,**kwargs):
        if request.method == 'POST':
            print(request)
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serialzer = StudentModelSerializer(data=python_data)
            if serialzer.is_valid():
                serialzer.save()
                msg = {'msg': 'Data Created with model serializer'}
                json_data = JSONRenderer().render(msg)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serialzer.errors)
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request,id=None,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        # id = python_data.get('id',None)
        # if id is not None :
        stud = Student.objects.get(id=id)
        serialzer = StudentSerializer(stud, data=python_data)
        if serialzer.is_valid():
            serialzer.save()
            msg = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serialzer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request,id=None,*args,**kwargs):
        if id is not None:
            stud = Student.objects.get(id=id)
            stud.delete()
            msg = {'msg': str(id) + 'id Deleted'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        stud = Student.objects.all()
        stud.delete()
        msg = {'msg':  'All Data Deleted'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')






def single_student_view(request,pk):
    stud = Student.objects.get(id=pk)
    serialized = StudentSerializer(stud)
    json_data = JSONRenderer().render(serialized.data)
    return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serialzer = StudentSerializer(data =python_data)
        if serialzer.is_valid():
            serialzer.save()
            msg = {'msg':'Data Created'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serialzer.errors)
        return HttpResponse(json_data, content_type='application/json')

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def create_student_form(request):


    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            data = {'id': int(fm.cleaned_data['id']),'name': fm.cleaned_data['name']}
            serialzer = StudentModelSerializer(data=data)
            if serialzer.is_valid():
                serialzer.save()
                msg = {'msg': 'Data Created with model serializer'}
                json_data = JSONRenderer().render(msg)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serialzer.errors)
            return HttpResponse(json_data, content_type='application/json')

    else:
        fm = StudentForm()
        print('get form')
    return render(request, 'pages/student.html', {'fm':fm})
