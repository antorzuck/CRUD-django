from django.shortcuts import render, redirect
from .models import * 

def home(request):
	if request.method== 'POST':
		datas= Girlfriend()
		datas.name = request.POST.get('name')
		datas.number = request.POST.get('number')
		datas.age = request.POST.get('age')
		datas.save()
		return redirect('/')
		
	data= Girlfriend.objects.all()
	return render(request, 'home.html', {'data':data})
	
def delete(request, id):
	if request.method == 'POST':
		remove= Girlfriend.objects.get(pk=id)
		remove.delete()
		return redirect('/')
		

def update(request, id):
	add= Girlfriend.objects.get(pk=id)
	if request.method == 'POST':
		add.name=request.POST.get('name')
		add.number = request.POST.get('number')
		add.age=request.POST.get('age')
		add.save()
		return redirect('/')
	return render(request, 'update.html',{'add':add})