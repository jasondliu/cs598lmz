import weakref
import threading
from functools import partial
from io import BytesIO, StringIO
import lxml
import lxml.etree
from lxml.etree import Element, SubElement
import HTMLParser
import urllib
import urllib2
import json
import re
import base64
import mimetypes
import string
from operator import itemgetter
import os
import os.path
import time

from openerp import SUPERUSER_ID
from openerp.tools.translate import _
from openerp.tools import (DEFAULT_SERVER_DATETIME_FORMAT,
                           DEFAULT_SERVER_DATE_FORMAT)

from urllib2 import HTTPError

from .tools import _parse_xml
from .tools import _parse_wiki
from .tools import ustr

from openerp import http
from openerp.http import request
from openerp.addons.web.controllers.main import Binary

from openerp import models, fields, api

# may be overridden
