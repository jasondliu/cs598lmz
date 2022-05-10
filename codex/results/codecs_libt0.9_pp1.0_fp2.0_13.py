import codecs
codecs.getwriter("utf-8")(sys.stdout)

from app import app

from picz.lazy import LazyLoader
from picz.picz import Picz
from picz.config import *

from flask.ext.cache import Cache


class Configuration(object):
    DEBUG = False
    SECRET_KEY = 'v4F4dW8dV7z4cX4uS2j2'
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024

    #base path for storing images
    #BASE_PATH = os.path.expanduser('~/pics')
    #URL_PATH = '/pics'

    # mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
    #MONGODB_HOST = "coco.netbox.es"
    MONGODB_HOST = "localhost"
    MONGODB_PORT = "27017"
    MONGODB_
