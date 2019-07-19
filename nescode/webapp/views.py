from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import customer, investment

# Create your views here.
def View(request,id=None):

   custlist=customer.objects.all()

   MyDict={'custlist':custlist}
   return render(request,'html_files/Admin.html',MyDict)

def view2(request,id=None):
   investlist = investment.objects.all()

   MyDict = {'investlist': investlist}
   return render(request, 'html_files/investment.html', MyDict)









