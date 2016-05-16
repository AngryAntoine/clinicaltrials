# -*- coding: UTF-8 -*-
# Create your views here.

from django.shortcuts import render
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
