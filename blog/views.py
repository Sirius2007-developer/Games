from django.http import Http404
from django.shortcuts import render
from .models import Product, Control, Remote, Quote, About, Thing


# Create your views here.
def about(request):
    about = About.objects.all()
    context = {
        "about": about,
    }
    return render(request, "about.html", context=context)

def contact(request):
    return render(request, "contact.html", context={})

def index(request):
    control = Control.objects.all()
    product = Product.objects.all()
    quote = Quote.objects.all()
    remote = Remote.objects.all()
    about = About.objects.all()
    thing = Thing.objects.all()
    context = {
        "control": control,
        "product": product,
        "quote": quote,
        "remote": remote,
        "about": about,
        "thing": thing,
    }
    return render(request, "index.html", context=context)

def product(request):
    product = Product.objects.all()
    remote = Remote.objects.all()
    thing = Thing.objects.all()
    context = {
        "product": product,
        "remote": remote,
        "thing": thing,
    }
    return render(request, "product.html", context=context)

def remot(request):
    remote = Remote.objects.all()
    thing = Thing.objects.all()
    context = {
        "remote": remote,
        "thing": thing,
    }
    return render(request, "remot.html", context=context)

def video(request):
    product = Product.objects.all()
    context = {
        "product": product,
    }
    return render(request, "video.html", context=context)

def prodetailview(request, id):
    try:
        pro = Quote.objects.get(id=id)
        context = {
            "pro": pro,
        }
    except pro.DoesNotExists:
        raise Http404("No product found")
    return render(request, "prodetail.html", context=context)
