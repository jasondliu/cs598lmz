import mmap
import os
import re
import sys
import time
import traceback
import urllib2

from datetime import datetime
from threading import Thread, Lock

try:
    import simplejson as json
except ImportError:
    import json

try:
    import pyinotify
except ImportError:
    pyinotify = None

try:
    import pwd, grp
except ImportError:
    pwd, grp = None, None

try:
    import fcntl
except ImportError:
    fcntl = None

try:
    import ssl
except ImportError:
    ssl = None

try:
    from hashlib import md5
except ImportError:
    from md5 import md5

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

try:
    from collections import defaultdict
except ImportError:
    class defaultdict(dict):
        def __init__(self, default_factory=None, *a, **kw):
            if (
