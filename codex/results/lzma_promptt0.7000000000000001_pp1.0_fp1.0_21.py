import lzma
# Test LZMADecompressor to see if the LZMA library is available
try:
    lzma.LZMADecompressor()
    HAS_LZMA = True
except OSError:
    HAS_LZMA = False

from zipfile import is_zipfile, ZipFile
from tempfile import mktemp
from email.utils import parsedate_tz, mktime_tz
from datetime import datetime
from os import getcwd
from os.path import basename, exists, dirname
from urllib.parse import urlsplit
from shutil import copyfileobj
from threading import Thread
from requests.compat import urljoin, urlparse
from requests.sessions import Session
from zipstream import ZipStream
from requests.models import Response
from requests.utils import from_key_val_list
from requests.structures import CaseInsensitiveDict
from requests.exceptions import RequestException
from requests.adapters import BaseAdapter

from .exceptions import BadZipFile, IncompleteZipFile
from .compat import StringIO, URLError, BytesIO
from .utils import mkdir
