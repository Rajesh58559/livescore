from django.shortcuts import render,redirect
from .models import Match

# Create your views here.


def home(request):
    det=Match.objects.all()
    if request.method=='POST':
        mname=request.POST.get('mname','')
        mcount=request.POST.get('mcount','')
        team1=request.POST.get('team1','')
        team2 = request.POST.get('team2', '')
        icon=request.FILES['icon']
        icons=request.FILES['icons']
        venue = request.POST.get('venue', '')
        time = request.POST.get('time', '')
        date = request.POST.get('date', '')
        match=Match(mname=mname,mcout=mcount,teams=team1,team2=team2,icon1=icon,icon2=icons,venue=venue,date=date,time=time)
        match.save()
    return render(request,"home.html",{'det':det})

def delete(request,id):
    if request.method=='POST':
        dele = Match.objects.get(id=id)
        dele.delete()
        return redirect('/')
    return render(request,'delete.html')




