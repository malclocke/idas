from django.conf.urls import patterns, url

urlpatterns = patterns('spectra.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<spectrum_id>\d+)/$', 'show', name='show'),
    url(r'^(?P<spectrum_id>\d+)/plot.png$', 'plot', name='plot'),
    url(r'^(?P<spectrum_id>\d+)/plot-small.png$', 'plot_small', name='plot_small'),
    url(r'^upload/$', 'upload', name='upload'),
)
