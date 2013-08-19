from django.conf import settings
from django.utils.cache import patch_vary_headers

HTTP_SERVER_HOST = 'HTTP_HOST'
HOST_PORT_SEPARATOR = ':'

class MultiHostMiddleware(object):

    def process_request(self, request):
        if not HTTP_SERVER_HOST in request.META:
            request.urlconf = settings.ROOT_URLCONF
            return
        host = request.META[HTTP_SERVER_HOST]
        host = self._host_remove_port(host)
        try:
            request.urlconf = settings.MULTIHOST_URLCONF[host]
        except KeyError:
            request.urlconf = settings.ROOT_URLCONF

    # process_response to get Django's cache framework to vary per host 
    def process_response(self, request, response):
        if getattr(request, 'urlconf', None):
            patch_vary_headers(response, ('Host',))
        return response

    @staticmethod
    def _host_remove_port(host):
        ''' Ignore default port number, if present '''
        if HOST_PORT_SEPARATOR in host:
            host = host.split(HOST_PORT_SEPARATOR)[0]
        return host
