import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup

from . import config
from . import util
from . import version

# TODO:
# - Add a way to specify the number of threads to use.
# - Add a way to specify the number of retries to use.
# - Add a way to specify the timeout to use.
# - Add a way to specify the user agent to use.
# - Add a way to specify the referer to use.
# - Add a way to specify the cookie to use.
# - Add a way to specify the proxy to use.
# - Add a way to specify the output directory.
# - Add a way to specify the output filename.
# - Add a way to specify the output format.
# - Add a way to specify the output quality.
# - Add a way to specify the output extension.
# - Add a way to specify the output template.
# - Add a way to specify the output template for playlists.
# - Add a way to
