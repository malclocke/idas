from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from spectra import views
from spectra.models import Spectrum

urlpatterns = patterns('spectra.views',
    url(r'^$',
        ListView.as_view(
            queryset=Spectrum.objects.all(),
            context_object_name='spectra',
            template_name='spectra/index.html'),
        name='index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Spectrum,
            template_name='spectra/show.html'),
        name='show'),
    url(r'^(?P<spectrum_id>\d+)/plot.png$', 'plot', name='plot'),
    url(r'^(?P<spectrum_id>\d+)/plot-small.png$', 'plot_small', name='plot_small'),
    url(r'^(?P<spectrum_id>\d+)/download$', 'download', name='download'),
    url(r'^upload/$', 'upload', name='upload'),
)
