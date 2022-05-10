import socket

import tornado.httpserver
import tornado.ioloop
import tornado.web

from tornado.options import options

from sessions.handlers import SessionMixin

from . import settings
from . import urls
from . import db
from . import logger


parser = argparse.ArgumentParser(description='Serve pages')
parser.add_argument('-H', '--host', default=settings.HOST,
                    help='bind to this host')
parser.add_argument('-p', '--port', default=settings.PORT, type=int,
                    help='bind to this port')
parser.add_argument('--debug', '-d', action='store_true', help='run in debug mode')
options = parser.parse_args()

if options.debug:
    # enable debug mode
    settings.DEBUG = options.debug
    settings.LOCAL_STORAGE_PATH = os.path.join(os.path.dirname(__file__), 'local_storage')
    settings.TEMPLATES_PATH = os.path.join(os.path.dirname
