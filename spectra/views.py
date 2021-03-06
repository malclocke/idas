from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from spectra.models import Spectrum
from spectra.forms import SpectrumForm
from specreduce.specreduce import BessSpectra

@login_required
def upload(request):
    if request.method == 'POST':
        form = SpectrumForm(request.POST, request.FILES)
        if form.is_valid():
            spectrum = form.save(commit=False)
            spectrum.user = request.user
            spectrum.save()
            return HttpResponseRedirect(reverse('spectra:index'))

    else:
        form = SpectrumForm()

    return render_to_response('spectra/upload.html', {'form': form},
        context_instance=RequestContext(request))

def plot(request, spectrum_id):
    spectrum = get_object_or_404(Spectrum, pk=spectrum_id)
    response=HttpResponse(content_type='image/png')
    spectrum.print_png(response)
    return response

def plot_small(request, spectrum_id):
    spectrum = get_object_or_404(Spectrum, pk=spectrum_id)
    response=HttpResponse(content_type='image/png')
    spectrum.print_png(response, figsize=(64,64), style='compact')
    return response

def download(request, spectrum_id):
    spectrum = get_object_or_404(Spectrum, pk=spectrum_id)
    response=HttpResponse(spectrum.fits, content_type='image/fits')
    response['Content-Disposition'] = 'attachment; filename=%s' % spectrum.fits.name.split('/')[-1]
    return response
