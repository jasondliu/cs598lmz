import mmap
import os
import re
import requests
import subprocess
import sys
import tempfile
import urllib
import urllib2

from multiprocessing import Pool

try:
    from urlparse import urlparse
except ImportError:
    # python3
    from urllib.parse import urlparse

import pycurl

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

try:
    from distutils.version import LooseVersion
except ImportError:
    from distutils.util import LooseVersion

try:
    from bdconfig.decorators import Log
except ImportError:
    from decorators import Log

try:
    from bdconfig.commons import AppLogger
except ImportError:
    from commons import AppLogger

try:
    from bdconfig.host_utils import HostUtils
except ImportError:
    from host_utils import HostUtils

try:
    from bdconfig.url_utils import URLUtils
except ImportError:
    from url_utils import URL
