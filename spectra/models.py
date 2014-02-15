from django.db import models
from django.contrib.auth.models import User
import pyfits
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from specreduce.specreduce import BessSpectra
from spectra.extra import OneDimensionalSpectrumFileField

class Spectrum(models.Model):
    fits = OneDimensionalSpectrumFileField(upload_to='spectra')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.target_name()

    def target_name(self):
        return self.header_value('OBJECT', 'OBJNAME')

    def date_obs(self):
        return self.header_value('DATE-OBS')

    def observer(self):
        return self.header_value('OBSERVER')

    def date_obs(self):
        return self.header_value('DATE-OBS')

    def instrument(self):
        return self.header_value('BSS_INST', 'INSTRUME')

    def site(self):
        return self.header_value('BSS_SITE', 'SITE')

    def units(self):
        return self.header_value('CUNIT1')

    def header(self):
        return pyfits.getheader(self.fits.path)

    def hdulist(self):
        return pyfits.open(self.fits.path)

    def header_value(self, *keywords):
        header = self.header()
        for keyword in keywords:
            if keyword in header:
                return header[keyword]

    def bess_spectrum(self):
        return BessSpectra(self.hdulist())

    def wavelength_start(self):
        return self.bess_spectrum().wavelengths()[0]

    def wavelength_end(self):
        return self.bess_spectrum().wavelengths()[-1]

    def print_png(self, receiver, figsize=(640,480), style=None):
        dpi = 72.
        x, y = figsize
        x = x / dpi
        y = y / dpi
        fig=Figure(figsize=(x,y), dpi=dpi, facecolor='white')
        ax=fig.add_subplot(111)
        if style == 'compact':
            ax.autoscale_view('tight')
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
        self.bess_spectrum().plot_onto(ax)
        canvas=FigureCanvas(fig)
        canvas.print_png(receiver)

