from django.shortcuts import render
#from . models import Task
# # Create your views here.
# def home(request):
#     if request.method=='POST':
#         matchname=request.POST.get('matchname','')
#         matchnum=request.POST.get('matchnum','')
#         match=Task(name=matchname,count=matchnum)
#         match.save()
#     return render(request,"home.html")
def demo(request):
    return render(request,"home.html")