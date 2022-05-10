import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import re
import sys
import shutil
import zipfile
from os.path import join

import requests
import lxml.html
from lxml.cssselect import CSSSelector

from six.moves.urllib.parse import urlparse
from six import text_type as unicode

from . import __version__
from . import db
from . import utils
from . import utils as u
from . import tsv
from . import models
from . import settings
from . import exceptions
from . import log

from .utils import urlquote, urljoin, quote
from .utils import urlopen
from .utils import urlretrieve, urlcleanup

from .log import logger

from .utils import get_requests_session

from .models import Dataset, Release, Resource

from . import ckanclient
from . import ckan_api

from .utils import make_dir, download_file
from .utils import unzip_file, unrar_file, untar_file
from .utils import get_cache
