import select
import socket
import sys
import time
import traceback
import urllib2
import urlparse

from wsgiref.handlers import format_date_time
from wsgiref.headers import Headers
from wsgiref.simple_server import make_server, WSGIRequestHandler

from . import __version__
from . import config
from . import logger
from . import utils
from . import wsgi

log = logger.get_logger(__name__)


def get_application(app_id):
    """
    Get the WSGI application for the given app_id.

    :param app_id: The application identifier.
    :returns: The WSGI application.
    """
    if app_id not in config.applications:
        raise ValueError('Unknown application: %r' % app_id)
    app = config.applications[app_id]
    if app.get('type') == 'wsgi':
        return wsgi.get_wsgi_application(app_id)
    else:
        raise ValueError
