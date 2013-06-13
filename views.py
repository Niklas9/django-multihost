import django.shortcuts as shortcuts
import django_multihost.settings as settings


def multihost1(request):
	template_uri = '%s/index.html' % settings.TEMPLATE_MULTIHOST1_DIR
	return shortcuts.render_to_response(template_uri)

def multihost2(request):
    template_uri = '%s/index.html' % settings.TEMPLATE_MULTIHOST2_DIR
    return shortcuts.render_to_response(template_uri)

def multihost3(request):
    template_uri = '%s/index.html' % settings.TEMPLATE_MULTIHOST3_DIR
    return shortcuts.render_to_response(template_uri)