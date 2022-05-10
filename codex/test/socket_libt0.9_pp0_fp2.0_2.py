import socket
from urllib.parse import urljoin

from django import template
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import reverse
from django.urls import get_script_prefix
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

register = template.Library()


@register.simple_tag(takes_context=True)
def absolute_url(context, url=None, keep_query=False, full=False):
    """Return the absolute URL.

    :return: the absolute URL
    """
    request = context.get('request', None)

    if url is None:
        url = request.get_full_path()
    elif 'request' in dir(url):
        url = url.request.get_full_path()
