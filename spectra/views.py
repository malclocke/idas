from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from spectra.models import Spectrum
from specreduce.specreduce import BessSpectra


def upload(request):
  if request.method == 'POST':
    spectrum = Spectrum(fits=request.FILES['fits'])
    spectrum.save()
    return HttpResponseRedirect(reverse('spectra:index'))
  else:
    context = {}
    return render_to_response('spectra/upload.html', context,
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
