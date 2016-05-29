# -*- coding: UTF-8 -*-
# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Condition, TherapeuticArea, StudyIdentifiers, Sponsor


def study(request):
    conditions = Condition.objects.all()
    therapeutic_area = TherapeuticArea.objects.all()
    study_description = StudyIdentifiers.objects.all()
    sponsor = Sponsor.objects.all()
    return render(request, 'study/study_home.html', {'conditions': conditions,
                                                     'therapeutic_areas': therapeutic_area,
                                                     'study_descriptions': study_description,
                                                     'sponsors': sponsor})


def study_details(request):
    #     studies = get_object_or_404(StudyIdentifiers, id=study_id)
    #     # food_detail = get_object_or_404(Food, id=food_id)
    #     return render(request, 'study/study_details.html',
    #                   {'studies': studies})
    return render(request, 'study/study_detail.html')


def basic_information(request):
    #     studies = get_object_or_404(StudyIdentifiers, id=study_id)
    #     # food_detail = get_object_or_404(Food, id=food_id)
    #     return render(request, 'study/study_details.html',
    #                   {'studies': studies})
    return render(request, 'study/basic_information.html')


def eligibility(request):
    #     studies = get_object_or_404(StudyIdentifiers, id=study_id)
    #     # food_detail = get_object_or_404(Food, id=food_id)
    #     return render(request, 'study/study_details.html',
    #                   {'studies': studies})
    return render(request, 'study/eligibility.html')


def contacts(request):
    #     studies = get_object_or_404(StudyIdentifiers, id=study_id)
    #     # food_detail = get_object_or_404(Food, id=food_id)
    #     return render(request, 'study/study_details.html',
    #                   {'studies': studies})
    return render(request, 'study/contacts.html')


def place(request):
    #     studies = get_object_or_404(StudyIdentifiers, id=study_id)
    #     food_detail = get_object_or_404(Food, id=food_id)
    #     return render(request, 'study/study_details.html',
    #                   {'studies': studies})
    return render(request, 'study/place.html')
