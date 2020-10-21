from django.shortcuts import render,redirect

# Create your views here.
from .models import Stock
from .form import StockCreateForm
def home(request):
    text="example text"
    context={"txt":text}
    return render(request,"home.html",context)

def list_item(request):
    text = "The following is a list of items available in the store"
    queryset=Stock.objects.all()
    context={"txt":text,"queryset":queryset}
    return render(request,"list_items.html",context)

def add_item(request):
    print("**********************beginnning")
    text = "enter the following details to add an item into the inventory"
    form = StockCreateForm(request.POST or None)
    print("*******************************midddle")
    if form.is_valid():
        print("********************in the form")
        form.save()
        return redirect("/list")
    
    context = {
		"form": form,
		"title": text,
	}
    print("****************************************end")
    return render(request, "add_item.html", context)