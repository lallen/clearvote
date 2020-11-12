from django.shortcuts import render

from .models import New

# Create your views here.
def frontpage(request):
    news = New.objects.all()
    return render(request, 'blog/frontpage.html', {'news':news})
