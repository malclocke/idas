from django import forms
from spectra.models import Spectrum

class SpectrumForm(forms.ModelForm):
    class Meta:
        model = Spectrum
