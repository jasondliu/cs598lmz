import socket
import ssl

from io import StringIO

try:
    from urllib.parse import urlparse, urljoin, urlunparse, urlencode
    from urllib.request import urlopen
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse, urljoin, urlunparse
    from urllib import urlencode
    from urllib2 import urlopen, HTTPError

import requests

## libs
import pkg_resources
pkg_resources.require('waterbutler')

from waterbutler.core import exceptions as wbexceptions
from waterbutler.core import streams
from waterbutler.core.utils import (
    BracedString,
    build_url,
    http_date,
    waterbutler_path_to_os_path,
    version_tuple,
    encode_url_component,
    decode_url_component,
)
from waterbutler.core import constants
from waterbutler.providers.filesystem.metadata import BaseFileMetadata, BaseFolderMetadata
from water
