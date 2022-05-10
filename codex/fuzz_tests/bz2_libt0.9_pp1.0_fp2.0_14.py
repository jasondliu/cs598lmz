import bz2
bz2c = bz2.compress
bz2u = bz2.decompress

from cStringIO import StringIO
from math import log
from Queue import Queue
from threading import Thread
from time import time

from pywikibot import translate

from wp import FAMILY, i18n, printException
import wp

from wp.cache.main import CacheAPI
from wp.data.base import API
from wp.data.revisions import Revision
from wp.data.titlesearch import PlusSearch
from wp.media import imagedim, SVGWikiImage
from wp.media.mw import MWImageInfo
from wp.media.utils import image_uri
from wp.net.HTTP import prefix_uri
from wp.net.virtua import VirtualAPI
from wp.net.virtua.api import batch_request
from wp.paraminfo.main import ParamInfo
from wp.xmlrpc.reader import XMLRPCReader
from wp.xmlrpc.upload import XMLRPCUpload

from wp.
