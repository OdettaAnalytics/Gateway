from __future__ import unicode_literals
from django.db import models
from django import forms


class Chi2Test(models.Model):
    fname = models.CharField(max_length=200, blank=True)
    chi2dof = models.FloatField(null=True, blank=True)
    chi2dof_bin = models.FloatField(null=True, blank=True)
    dof = models.IntegerField(null=True, blank=True)
    dofb = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'chi2test'


class Fluxvals(models.Model):
    m_id = models.IntegerField(primary_key=True)
    wavelength = models.FloatField()
    luminosity = models.FloatField(null=True, blank=True)
    photon_count = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'fluxvals'


class MetaDd2D(models.Model):
    m_id = models.BigIntegerField(primary_key=True)
    modelname = models.CharField(max_length=40, blank=True)
    modeltype = models.CharField(max_length=40, blank=True)
    modeldim = models.SmallIntegerField(null=True, blank=True)
    t_expl = models.FloatField(null=True, blank=True)
    phi = models.FloatField(null=True, blank=True)
    mu = models.FloatField(null=True, blank=True)
    mass_wd = models.FloatField(null=True, blank=True)
    percent_carbon = models.FloatField(null=True, blank=True)
    percent_oxygen = models.FloatField(null=True, blank=True)
    n_ignit = models.IntegerField(null=True, blank=True)
    r_min_ignit = models.FloatField(null=True, blank=True)
    cos_alpha = models.FloatField(null=True, blank=True)
    stdev = models.FloatField(null=True, blank=True)
    ka_min = models.FloatField(null=True, blank=True)
    rho_min = models.FloatField(null=True, blank=True)
    rho_max = models.FloatField(null=True, blank=True)
    comments = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'meta_dd2d'


class Models(models.Model):
    m_type_id = models.SmallIntegerField(primary_key=True)
    modeltype = models.CharField(max_length=40, blank=True)
    modeldim = models.SmallIntegerField(null=True, blank=True)
    date_entered = models.DateField(null=True, blank=True)
    citation = models.CharField(max_length=200, blank=True)
    sntype = models.CharField(max_length=10, blank=True)
    m_type_id = models.SmallIntegerField(null=True, blank=True, primary_key=True)

    class Meta:
        db_table = 'models'


class SearchForm(forms.Form):
    m_id = forms.IntegerField(required=False, label=u'Model ID')
    percent_oxygen = forms.FloatField(required=False, label=u'Percent Carbon')
    percent_carbon = forms.FloatField(required=False, label=u'Percent Oxygen')
