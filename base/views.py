from django.shortcuts import render

# Create your views here.
# ===============================================================
# home
# ===============================================================
def home(request):
    context = {}
    return render(request, 'base/home.html', context)

# ===============================================================
# about
# ===============================================================
def about(request):
    context = {}
    return render(request, 'base/about.html', context)

# ===============================================================
# services
# ===============================================================
def services(request):
    context = {}
    return render(request, 'base/services.html', context)

def service(request):
    context = {}
    return render(request, 'base/service.html', context)

# ===============================================================
# contact
# ===============================================================
def contact(request):
    context = {}
    return render(request, 'base/contact.html', context)

# ===============================================================
# faq
# ===============================================================
def faq(request):
    context = {}
    return render(request, 'base/faq.html', context)

# ===============================================================
# team
# ===============================================================
def teams(request):
    context = {}
    return render(request, 'base/team.html', context)

def team(request):
    context = {}
    return render(request, 'base/team-single.html', context)

# ===============================================================
# blog
# ===============================================================
def blogs(request):
    context = {}
    return render(request, 'base/blogs.html', context)

def blog(request):
    context = {}
    return render(request, 'base/blog.html', context)