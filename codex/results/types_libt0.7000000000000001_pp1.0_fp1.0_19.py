import types
types.FunctionType = types.MethodType

import sys
import os
import os.path
import time
import threading
import re
import urllib
import urllib2
import urlparse
import logging
import socket
import shutil
import subprocess
import tempfile

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

try:
    import json
except ImportError:
    import simplejson as json

try:
    import mechanize
except ImportError:
    logging.getLogger().error('mechanize not installed, see '
        'http://wwwsearch.sourceforge.net/mechanize/')
    sys.exit(1)

__version__ = '0.91'

USER_AGENT = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) ' \
    'Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13'

SERVER_ADDRS = [
