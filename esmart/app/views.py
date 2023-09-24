from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from app.models import Member
# Create your views here.
def index(request):
    return render(request,'app/index.html')

def create(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        member = Member(firstname=firstname, lastname=lastname)
        member.save()
        JsonResponse = JsonResponse({'success': True})
        return redirect('/')
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})