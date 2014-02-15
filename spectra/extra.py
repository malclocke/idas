from django.db.models import FileField
from django import forms
from django.utils.translation import ugettext as _
import pyfits

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^spectra\.extra\.OneDimensionalSpectrumFileField"])
class OneDimensionalSpectrumFileField(FileField):

    def clean(self, *args, **kwargs):
        data = super(OneDimensionalSpectrumFileField, self).clean(*args, **kwargs)
        # This will raise IOError if there is a parse failure
        try:
            hdulist = pyfits.open(data.file)
        except IOError as e:
            raise forms.ValidationError(_('Unable to parse FITS file: %s' % e))
        return data
