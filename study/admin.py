from django.contrib import admin
from .models import *
from django.utils.translation import ugettext_lazy as _


class ConditionAdmin(admin.ModelAdmin):
    list_display = ['name']
    # prepopulated_fields = {"slug": ("name",)}
    fieldsets = [
                (_('Item'),             {'fields': ['name']}),
                # ('Date information', {'fields': [('created','updated')], 'classes': ['collapse']}),
                (_('Description'),      {'fields': ['description']}),
                # ('Medias',           {'fields': ['image']}),
                # ('Metas',            {'fields': ['status','price','stock']}),
            ]

admin.site.register(Condition, ConditionAdmin)


# class TherapeuticAreaAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     # prepopulated_fields = {"slug": ("name",)}

admin.site.register(TherapeuticArea)


class GeneralInformationAdmin(admin.ModelAdmin):
    pass

admin.site.register(GeneralInformation, GeneralInformationAdmin)


class StudyDescriptionAdmin(admin.ModelAdmin):
    pass

admin.site.register(StudyIdentifiers, StudyDescriptionAdmin)


class SponsorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sponsor, SponsorAdmin)


class MedicalConditionAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(MedicalCondition, MedicalConditionAdmin)


# class AllStudyRelatedMaterialsAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(AllStudyRelatedMaterials, AllStudyRelatedMaterialsAdmin)


class InvestigationalProductsAdmin(admin.ModelAdmin):
    pass

admin.site.register(InvestigationalProducts, InvestigationalProductsAdmin)


class ComparatorsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comparators, ComparatorsAdmin)


class StudyRelatedMaterialsAdmin(admin.ModelAdmin):
    pass

admin.site.register(StudyRelatedMaterials, StudyRelatedMaterialsAdmin)


class InclusionCriteriaAdmin(admin.ModelAdmin):
    pass

admin.site.register(InclusionCriteria, InclusionCriteriaAdmin)


class ExclusionCriteriaAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExclusionCriteria, ExclusionCriteriaAdmin)


class EligibilityAdmin(admin.ModelAdmin):
    search_fields = ['name', 'inclusion_criteria']
    # pass

admin.site.register(Eligibility, EligibilityAdmin)


class ContactsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contacts, ContactsAdmin)


class CountyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, CountyAdmin)


class CityAdmin(admin.ModelAdmin):
    pass

admin.site.register(City, CityAdmin)


class PrincipalInvestigatorAdmin(admin.ModelAdmin):
    pass

admin.site.register(PrincipalInvestigator, PrincipalInvestigatorAdmin)


class HeadOfDepartmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(HeadOfDepartment, HeadOfDepartmentAdmin)


class PlaceAddressAdmin(admin.ModelAdmin):
    pass

admin.site.register(PlaceAddress, PlaceAddressAdmin)


class ClinicalStudySiteAdmin(admin.ModelAdmin):
    pass

admin.site.register(ClinicalStudySite, ClinicalStudySiteAdmin)


class MedicalInstitutionPhoneNumberAdmin(admin.ModelAdmin):
    pass

admin.site.register(MedicalInstitutionPhoneNumber, MedicalInstitutionPhoneNumberAdmin)

class StudyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Study, StudyAdmin)
