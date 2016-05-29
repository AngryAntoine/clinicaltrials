from django.shortcuts import render


def about_clinical_research(request):
    return render(request, "home/about_clinical_research.html")
