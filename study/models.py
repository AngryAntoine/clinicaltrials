# coding=utf-8
from __future__ import unicode_literals
from django.db import models
# from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Condition(models.Model):
    name = models.CharField(_('condition name'), max_length=100, null=True, blank=True)
    description = models.TextField(_('description'), max_length=4096, null=True, blank=True)

    # slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('condition')
        verbose_name_plural = _('conditions')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class TherapeuticArea(models.Model):
    CHOOSE_CONDITION = _('Choose condition')
    ANDROLOGY = _('Andrology')
    ASTHMA = _('Asthma & Allergy')
    CARDIOLOGY = _('Cardiology & Vascular Diseases')
    DERMATOLOGY = _('Dermatology')
    DENTISTRY = _('Dentistry')
    ENDOCRINOLOGY = _('Endocrinology')
    GASTROENTOROLOGY = _('Gastroentorology')
    GERONTOLOGY = _('Gerontology & Geriatrics')
    HEALTHY_VOLUNTEERS = _('Healthy Volunteers')
    HEMATOLOGY = _('Hematology')
    HEPATOLOGY = _('Hepatoogy')
    IMMUNOLOGY = _('Immunology')
    INFECTIOUS_DISEASES = _('Infectious Diseases')
    MEDICAL_DEVICE = _('Medical Device')
    NEUROLOGY = _('Neurology')
    NEPHROLOGY = _('Nephrology')
    OBSTETRICS = _('Obstetrics & Gynaecology (OB&GYN)')
    OCOLOGY = _('Oncology')
    OPHTHALMOLOGY = _('Ophthalmology')
    OTORHINOLARYNGOLOGY = _('Otorhinolaryngology')
    PEDIATRICS = _('Pediatrics')
    PLASTIC_SURGERY = _('Plastic Surgery')
    PSYCHIATRY = _('Psychiatry')
    PULMONOLOGY = _('Pulmonology')
    REPRODUCTIVE_MEDICINE = _('Reproductive Medicine')
    RHEUMATOLOGY = _('Rheumatology')
    SURGERY = _('Surgery')
    TRAUMATOLOGY = _('Traumatology')
    UROLOGY = _('Urology')
    VENEROLOGY = _('Venerology')
    THERAPEUTIC_AREA_CHOICES = (
        (CHOOSE_CONDITION, _('Choose condition')),
        (ANDROLOGY, _('Andrology')),
        (ASTHMA, _('Asthma & Allergy')),
        (CARDIOLOGY, _('Cardiology & Vascular Diseases')),
        (DERMATOLOGY, _('Dermatology')),
        (DENTISTRY, _('Dentistry')),
        (ENDOCRINOLOGY, _('Endocrinology')),
        (GASTROENTOROLOGY, _('Gastroentorology')),
        (GERONTOLOGY, _('Gerontology & Geriatrics')),
        (HEALTHY_VOLUNTEERS, _('Healthy Volunteers')),
        (HEMATOLOGY, _('Hematology')),
        (HEPATOLOGY, _('Hepatoogy')),
        (IMMUNOLOGY, _('Immunology')),
        (INFECTIOUS_DISEASES, _('Infectious Diseases')),
        (MEDICAL_DEVICE, _('Medical Device')),
        (NEUROLOGY, _('Neurology')),
        (NEPHROLOGY, _('Nephrology')),
        (OBSTETRICS, _('Obstetrics & Gynaecology (OB&GYN)')),
        (OCOLOGY, _('Oncology')),
        (OPHTHALMOLOGY, _('Ophthalmology')),
        (OTORHINOLARYNGOLOGY, _('Otorhinolaryngology')),
        (PEDIATRICS, _('Pediatrics')),
        (PLASTIC_SURGERY, _('Plastic Surgery')),
        (PSYCHIATRY, _('Psychiatry')),
        (PULMONOLOGY, _('Pulmonology')),
        (REPRODUCTIVE_MEDICINE, _('Reproductive Medicine')),
        (RHEUMATOLOGY, _('Rheumatology')),
        (SURGERY, _('Surgery')),
        (TRAUMATOLOGY, _('Traumatology')),
        (UROLOGY, _('Urology')),
        (VENEROLOGY, _('Venerology')),
    )
    name = models.CharField(_('decease name'), choices=THERAPEUTIC_AREA_CHOICES, max_length=100,
                            default='CHOOSE_CONDITION', null=True, blank=True)

    class Meta:
        verbose_name = _('therapeutic area')
        verbose_name_plural = _('therapeutic areas')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Disease(models.Model):
    name = models.CharField(_('disease name'), max_length=100, null=True, blank=True)
    therapeutic_area = models.ForeignKey(TherapeuticArea, verbose_name=_('therapeutic area'), blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('disease')
        verbose_name_plural = _('diseases')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class GeneralInformation(models.Model):
    name = models.ForeignKey(TherapeuticArea, max_length=100, null=True, blank=True)
    # slug = models.SlugField(max_length=200, db_index=True, unique=True)
    decease_name = models.ForeignKey(Disease, blank=True, null=True, verbose_name=_('decease_name'))
    protocol_title = models.CharField(_('protocol title'), max_length=200, null=True, blank=True)
    detail_description = models.TextField(_('detailed description'), null=True, blank=True)
    PHASE_I = 'I'
    PHASE_I_II = 'I/II'
    PHASE_I_III = 'I/III'
    PHASE_II = 'II'
    PHASE_II_III = 'II/III'
    PHASE_III = 'III'
    PHASE_III_IV = 'III/IV'
    PHASE_IV = 'IV'
    PHASE_CHOICES = (
        (PHASE_I, 'I'),
        (PHASE_I_II, 'I/II'),
        (PHASE_I_III, 'I/III'),
        (PHASE_II, 'II'),
        (PHASE_II_III, 'II/III'),
        (PHASE_III, 'III'),
        (PHASE_III_IV, 'III/IV'),
        (PHASE_IV, 'IV'),
    )
    phase = models.CharField(_('phase'), max_length=20, choices=PHASE_CHOICES, null=True, blank=True)
    INTERVENTIONAL = _('Interventional')
    NON_INTERVENTIONAL = _('Non-Interventional')
    STUDY_TYPE_CHOICES = (
        (INTERVENTIONAL, _('Interventional')),
        (NON_INTERVENTIONAL, _('Non-Interventional')),
    )
    study_type = models.CharField(_('study type'), max_length=50, choices=STUDY_TYPE_CHOICES, null=True, blank=True)
    ALLOCATION = _('Allocation')
    ENDPOINT_CLASSIFICATION = _('Endpoint Classification')
    INTERVENTION_MODEL = _('Intervention Model')
    MASKING = _('Masking')
    PRIMARY_PURPOSE = _('Primary Purpose')
    STUDY_DESIGN_CHOICES = (
        (ALLOCATION, _('Allocation')),
        (ENDPOINT_CLASSIFICATION, _('Endpoint Classification')),
        (INTERVENTION_MODEL, _('Intervention model')),
        (MASKING, _('Masking')),
        (PRIMARY_PURPOSE, _('Primary purpose')),
    )
    study_design = models.CharField(_('study design'), max_length=50, choices=STUDY_DESIGN_CHOICES, null=True,
                                    blank=True)
    purpose = models.CharField(_('purpose'), max_length=10000, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'general information'
        verbose_name_plural = 'general information'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Sponsor(models.Model):
    name = models.CharField(_('sponsor name'), max_length=100, null=True, blank=True)
    address = models.CharField(_('address'), max_length=100, null=True, blank=True)
    phone = models.IntegerField(_('phone'), null=True, blank=True)
    email = models.CharField(_('email'), max_length=100, null=True, blank=True)
    link = models.CharField(_('link'), max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Company(models.Model):
    name = models.CharField(_('company name'), max_length=100, null=True, blank=True)
    address = models.CharField(_('address'), max_length=100, null=True, blank=True)
    phone = models.IntegerField(_('phone'), null=True, blank=True)
    email = models.CharField(_('email'), max_length=100, null=True, blank=True)
    link = models.CharField(_('link'), max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('company')
        verbose_name_plural = _('companies')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class StudyIdentifiers(models.Model):
    # study_condition = models.ForeignKey(Condition, verbose_name=_('study condition'))
    # therapeutic_area = models.ForeignKey(TherapeuticArea, verbose_name=_('therapeutic area'))
    sponsor_protocol_number = models.CharField(_('Sponsor\'s protocol number'), max_length=100, null=True, blank=True)
    clinical_trials_com_ua_identifier = models.CharField(_('ClinicalTrials.com.ua Identifier'), max_length=100,
                                                         blank=True, null=True)
    clinical_trials_gov_identifier = models.CharField(_('ClinicalTrials.gov Identifier'), max_length=100, blank=True,
                                                      null=True)
    clinical_trials_gov_link = models.CharField(_('ClinicalTrials.gov link'), max_length=200, blank=True, null=True)
    eudract = models.CharField(_('EudraCT number'), max_length=100, blank=True, null=True)
    eudract_link = models.CharField(_('EudraCT link'), max_length=200, blank=True, null=True)
    moh_of_ukraine = models.CharField(_('MOH of Ukraine'), max_length=100, blank=True, null=True)
    moh_of_ukraine_link = models.CharField(_('MOH of Ukraine link'), max_length=200, blank=True, null=True)
    sponsor_card = models.ForeignKey(Sponsor, verbose_name=_('sponsor, country'), null=True, blank=True)
    company_card = models.ForeignKey(Company, verbose_name=_('Company that controls conducting of clinical '
                                                             'study in Ukraine'), null=True, blank=True)
    estimated_enrollment_clinicaltrials_overall = models.IntegerField(
        _('Estimated enrollment in general according to clinicaltrials.com'), blank=True, null=True)
    estimated_enrollment_moh_ukraine_overall = models.IntegerField(
        _('Estimated enrollment in general according to MOH of Ukraine'), blank=True, null=True)
    estimated_enrollment_company_overall = models.IntegerField(_(
        'Estimated enrollment in general according to \"Company\"'), blank=True, null=True)
    estimated_enrollment_moh_ukraine = models.IntegerField(
        _('Estimated enrollment in Ukraine according to MOH of Ukraine'), blank=True, null=True)
    estimated_enrollment_company = models.IntegerField(_('Estimated enrollment in Ukraine according to "Company"'),
                                                       blank=True, null=True)
    enrollment_start_date_ukraine = models.DateTimeField(_('start date of enrolling patients in Ukraine'), blank=True,
                                                         null=True)
    NOT_RECRUITING_YET = _('Not recruiting yet')
    RECRUITING = _('Recruiting')
    INVITATION_RECRUITING = _('On invitation recruiting')
    NOT_RECRUITING = _('Not recruiting')
    STUDY_END = _('Study end')
    STUDY_PAUSE = _('Study pause')
    STUDY_TERMINATED_BEFORE_RECRUITING = _('Study terminated before recruiting')
    STUDY_STATUS_UNKNOWN = _('Study status unknown')
    NOT_HEALTHY_RECRUITS = _('Not healthy recruits')
    STATUS_CHOICES = (
        (NOT_RECRUITING_YET, _('Not recruiting yet')),
        (RECRUITING, _('Recruiting')),
        (INVITATION_RECRUITING, _('Invitation needed')),
        (NOT_RECRUITING, _('Not recruiting')),
        (STUDY_END, _('Study finished')),
        (STUDY_PAUSE, _('Study paused')),
        (STUDY_TERMINATED_BEFORE_RECRUITING, _('Study ended before recruiting')),
        (STUDY_STATUS_UNKNOWN, _('Unknown study status')),
        (NOT_HEALTHY_RECRUITS, _('Recruits with decease only'))
    )
    study_status = models.CharField(_('study status'), max_length=50, choices=STATUS_CHOICES, default=None, null=True)
    last_day_date = models.DateTimeField(_('study completion date'), null=True, blank=True)
    last_updated_date = models.DateTimeField(_('last updated date'), blank=True, null=True)

    # created_date = models.DateTimeField(default=timezone.now)

    # def clinical_trials_identifier(self):
    #     self.into_table_id = StudyIdentifiers.objects.get(self.id)

    class Meta:
        verbose_name = _('study identifier')
        verbose_name_plural = _('study identifiers')

    def __str__(self):
        return self.sponsor_protocol_number


@python_2_unicode_compatible
class InvestigationProducts(models.Model):
    form = models.CharField(max_length=100, null=True, blank=True)
    doze = models.CharField(max_length=100, null=True, blank=True)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'investigation product'
        verbose_name_plural = 'investigation products'

    def __str__(self):
        return self.form


@python_2_unicode_compatible
class Comparators(models.Model):
    form = models.CharField(_('form'), max_length=100, null=True, blank=True)
    doze = models.CharField(_('doze'), max_length=100, blank=True, null=True)
    manufacturer = models.CharField(_('manufacturer'), max_length=100, null=True, blank=True)
    country = models.CharField(_('country'), max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _('comparator')
        verbose_name_plural = _('comparators')

    def __str__(self):
        return self.form


@python_2_unicode_compatible
class StudyRelatedMaterials(models.Model):
    name = models.CharField(_('name'), max_length=100, null=True, blank=True)
    manufacturer = models.CharField(_('manufacturer'), max_length=100, null=True, blank=True)
    country = models.CharField(_('country'), max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('study related material')
        verbose_name_plural = _('study related materials')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class AllStudyRelatedMaterials(models.Model):
    name = models.CharField(_('name'), max_length=100, null=True, blank=True)
    investigation_products = models.ForeignKey(InvestigationProducts, verbose_name=_('investigation_products'),
                                               null=True, blank=True)
    comparators = models.ForeignKey(Comparators, verbose_name=_('comparators'), null=True, blank=True)
    study_related_materials = models.ForeignKey(StudyRelatedMaterials, verbose_name=_('study related materials'),
                                                null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('all study-related materials')
        verbose_name_plural = _('all study-related materials')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class InclusionCriteria(models.Model):
    name = models.CharField(_('name'), max_length=100, null=True, blank=True)
    description = models.TextField(_('description'), null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('inclusion criteria')
        verbose_name_plural = _('inclusion criteria')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ExclusionCriteria(models.Model):
    name = models.CharField(_('name'), max_length=100, null=True, blank=True)
    description = models.TextField(_('description'), null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('exclusion criteria')
        verbose_name_plural = _('exclusion criteria')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Eligibility(models.Model):
    name = models.CharField(_('name'), max_length=100, null=True, blank=True)
    age_from = models.PositiveIntegerField(_('age from'), null=True, blank=True)
    age_to = models.PositiveIntegerField(_('age to'), null=True, blank=True)
    FEMALE_AND_MALE = _('Female and Male')
    FEMALE = _('Female')
    MALE = _('Male')
    GENDER_CHOICE = (
        (FEMALE_AND_MALE, _('Female and Male')),
        (FEMALE, _('Female')),
        (MALE, _('Male'))
    )
    gender = models.CharField(_('gender'), max_length=20, choices=GENDER_CHOICE, null=True, blank=True)
    YES = _('Yes')
    NO = _('No')
    HEALTHY_VOLUNTEERS_CHOICES = (
        (YES, _('Yes')),
        (NO, _('No'))
    )
    healthy_volunteers = models.CharField(_('healthy volunteers'), max_length=5,
                                          choices=HEALTHY_VOLUNTEERS_CHOICES, null=True, blank=True)
    # inclusion_criteria = models.ForeignKey(InclusionCriteria, verbose_name=_('inclusion criteria'), null=True,
    #                                        blank=True)
    # exclusion_criteria = models.ForeignKey(ExclusionCriteria, verbose_name=_('exclusion criteria'), null=True,
    #                                        blank=True)
    inclusion_criteria = models.CharField(_('inclusion criteria'), max_length=10000, null=True, blank=True)
    exclusion_criteria = models.CharField(_('exclusion criteria'), max_length=10000, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('eligibility')
        verbose_name_plural = _('eligibility')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Contacts(models.Model):
    name = models.CharField(_('full name of contact person provided by Sponsor'), max_length=100, null=True, blank=True)
    phone = models.IntegerField(_('telephone number of contact person provided by Sponsor'), null=True, blank=True)
    fax = models.IntegerField(_('fax of contact person provided by Sponsor'), null=True, blank=True)
    email = models.CharField(_('email of contact person provided by Sponsor'), max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('contacts')
        verbose_name_plural = _('contacts')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Country(models.Model):
    name = models.CharField(_('name'), max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('contry')
        verbose_name_plural = _('countries')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class City(models.Model):
    name = models.CharField(_('name'), max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('city')
        verbose_name_plural = _('cities')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PrincipalInvestigator(models.Model):
    name = models.CharField(_('name'), max_length=100, null=True, blank=True)
    HD = _('Head of department')
    CMS = _('Candidate of Medical Sciences')
    CBS = _('Candidate of Biological Sciences')
    CPS = _('Candidate of Philosophical Sciences')
    MD = _('Doctor of Medicine (M.D.)')
    DBS = _('Doctor of Biological Sciences')
    DP = _('Doctor of Philosophy (PhD)')
    P = _('Professor')
    A = _('Academician')
    PD = _('PhD (Doctor of Pharmacy)')
    POSITION_CHOICES = (
        (HD, _('Head of department')),
        (CMS, _('Candidate of Medical Sciences')),
        (CBS, _('Candidate of Biological Sciences')),
        (CPS, _('Candidate of Philosophical Sciences')),
        (MD, _('Doctor of Medicine (M.D.)')),
        (DBS, _('Doctor of Biological Sciences')),
        (DP, _('Doctor of Philosophy (PhD)')),
        (P, _('Professor')),
        (A, _('Academician')),
        (PD, _('PhD (Doctor of Pharmacy)')),
    )
    position = models.CharField(_('position'), max_length=100, choices=POSITION_CHOICES, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('principal investigator')
        verbose_name_plural = _('principal investigators')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class HeadOfDepartment(models.Model):
    name = models.CharField(_('name'), max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('head of department')
        verbose_name_plural = _('head of department')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class PlaceAddress(models.Model):
    index = models.PositiveIntegerField(_('index'), null=True, blank=True)
    city = models.CharField(_('city'), max_length=100, null=True, blank=True)
    CITY = _('City')
    VILLAGE = _('Village')
    ADDRESS_CHOICES_I = (
        (CITY, _('City')),
        (VILLAGE, _('Village')),
    )
    settle_type = models.CharField(_('inhabited locality'), max_length=10, choices=ADDRESS_CHOICES_I, null=True,
                                   blank=True)
    STR = _('Street')
    SQR = _('Square')
    BLVD = _('Boulevard')
    LANE = _('Lane')
    AVENUE = _('Avenue')
    ADDRESS_CHOICES_II = (
        (STR, _('Street')),
        (SQR, _('Square')),
        (BLVD, _('Boulevard')),
        (LANE, _('Lane')),
        (AVENUE, _('Avenue'))
    )
    street_type = models.CharField(_('street type'), max_length=10, choices=ADDRESS_CHOICES_II, null=True, blank=True)
    street = models.CharField(_('street name'), max_length=50, null=True, blank=True)
    building = models.CharField(_('building number'), max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = _('place address')
        verbose_name_plural = _('place addresses')

    def __str__(self):
        return '{}, {}, {}'.format(self.index, self.street, self.city)


@python_2_unicode_compatible
class MedicalInstitutionPhoneNumber(models.Model):
    name = models.CharField(_('name'), max_length=100, null=True, blank=True)
    info_desk = models.CharField(_('information desk'), max_length=20, null=True, blank=True)
    registration_desk = models.CharField(_('registration desk'), max_length=20, null=True, blank=True)
    receptions_ward = models.CharField(_('reception ward'), max_length=20, null=True,
                                       blank=True)  # приймальне відділення
    phone_number = models.CharField(_('phone number'), max_length=20, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('medical institution phone number')
        verbose_name_plural = _('medical institution phone numbers')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ClinicalStudySite(models.Model):
    CRIMEA = _('Autonomous Republic of Crimea')
    CHERKASY = _('Cherkaska')
    CHERNIHIV = _('Chernihivska')
    CHERNIVTSI = _('Chernivetska')
    DNIPROPETROVSK = _('Dnipropetrovska')
    DONETSK = _('Donetska')
    IVANO_FRANKIVSK = _('Ivano-Frankivska')
    KHARKIV = _('Kharkivska')
    KHERSON = _('Khersonska')
    KHMELNYTSKYI = _('Khmelnytska')
    KIROVOHRAD = _('Kirovohradska')
    KYIV = _('Kyiv')
    KYIV_REGION = _('Kyivska')
    LUHANSK = _('Luhanska')
    LVIV = _('Lvivska')
    MYKOLAYIV = _('Mykolayivska')
    ODESA = _('Odeska')
    POLTAVA = _('Poltavska')
    RIVNE = _('Rivnenska')
    SUMY = _('Sumska')
    TERNOPIL = _('Ternopilska')
    VINNYTSIA = _('Vinnytska')
    LUTSK = _('Volynska')
    UZHHOROD = _('Zakarpatska')
    ZAPIRIZHZHIA = _('Zaporizka')
    ZHYTOMYR = _('Zhytomyrska')
    REGION_CHOICES = (
        (CRIMEA, _('Autonomous Republic of Crimea')),
        (CHERKASY, _('Cherkaska')),
        (CHERNIHIV, _('Chernihivska')),
        (CHERNIVTSI, _('Chernivetska')),
        (DNIPROPETROVSK, _('Dnipropetrovska')),
        (DONETSK, _('Donetska')),
        (IVANO_FRANKIVSK, _('Ivano-Frankivska')),
        (KHARKIV, _('Kharkivska')),
        (KHERSON, _('Khersonska')),
        (KHMELNYTSKYI, _('Khmelnytska')),
        (KIROVOHRAD, _('Kirovohradska')),
        (KYIV, _('Kyiv')),
        (KYIV_REGION, _('Kyivska')),
        (LUHANSK, _('Luhanska')),
        (LVIV, _('Lvivska')),
        (MYKOLAYIV, _('Mykolayivska')),
        (ODESA, _('Odeska')),
        (POLTAVA, _('Poltavska')),
        (RIVNE, _('Rivnenska')),
        (SUMY, _('Sumska')),
        (TERNOPIL, _('Ternopilska')),
        (VINNYTSIA, _('Vinnytska')),
        (LUTSK, _('Volynska')),
        (UZHHOROD, _('Zakarpatska')),
        (ZAPIRIZHZHIA, _('Zaporizka')),
        (ZHYTOMYR, _('Zhytomyrska')),
    )
    region = models.CharField(_('region'), max_length=20, choices=REGION_CHOICES, null=True, blank=True)
    city = models.ForeignKey(City, verbose_name=_('city'), null=True, blank=True)
    principal_investigator = models.ForeignKey(PrincipalInvestigator, verbose_name=_('principal investigator'),
                                               null=True, blank=True)
    principal_investigator_phone_number = models.CharField(_('principal investigator phone number'), max_length=20,
                                                           null=True, blank=True)
    medical_institution = models.TextField(_('medical institution'), max_length=200, null=True, blank=True)
    medical_institution_department = models.TextField(_('medical institution department'), max_length=200, null=True,
                                                      blank=True)
    head_of_department = models.ForeignKey(HeadOfDepartment, verbose_name='head of department', null=True, blank=True)
    site = models.CharField(_('web site'), max_length=100, null=True, blank=True)
    address = models.ForeignKey(PlaceAddress, verbose_name=_('address'), null=True, blank=True)
    phone_number = models.ForeignKey(MedicalInstitutionPhoneNumber, verbose_name='phone number', null=True, blank=True)
    medical_institution_department_phone_number = models.CharField(_('medical institution department phone number'),
                                                                   max_length=20, null=True, blank=True)
    medical_institution_department_fax = models.CharField(_('medical institution department fax'), max_length=20,
                                                          null=True, blank=True)
    medical_educational_institution = models.CharField(_('medical educational institution'), max_length=100, null=True,
                                                       blank=True)
    medical_educational_institution_department = models.CharField(_('medical educational institution department'),
                                                                  max_length=100, null=True, blank=True)
    medical_institution_contact_person_name = models.CharField(_('medical institution contact person name'),
                                                               max_length=100, null=True, blank=True)
    company_contact_person_name = models.CharField(_('company contact person name'), max_length=100, null=True,
                                                   blank=True)
    contact_person_phone_number = models.CharField(_('contact person phone number'), max_length=20, null=True,
                                                   blank=True)
    contact_person_fax = models.CharField(_('contact person fax'), max_length=20, null=True, blank=True)
    contact_person_email = models.CharField(_('contact person email'), max_length=100, null=True, blank=True)
    NRY = _('Not recruiting yet')
    R = _('Recruiting')
    NR = _('Not recruiting')
    RECRUITING_CHOICES = (
        (NRY, _('Not recruiting yet')),
        (R, _('Recruiting')),
        (NR, _('Not recruiting')),
    )
    recruiting_status_clinicaltrials = models.CharField(_('recruiting status clinicaltrials'), max_length=20,
                                                        choices=RECRUITING_CHOICES, null=True, blank=True)
    recruiting_status_moh = models.CharField(_('recruiting status MOH of Ukraine'), max_length=20, default=None,
                                             choices=RECRUITING_CHOICES, null=True, blank=True)
    recruiting_status_company = models.CharField(_('recruiting status company'), max_length=20, default=None,
                                                 choices=RECRUITING_CHOICES, null=True, blank=True)

    class Meta:
        verbose_name = _('place')
        verbose_name_plural = _('places')

    def __str__(self):
        return self.city
