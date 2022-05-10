import lzma
lzma.open

import os
import sys
import datetime
import subprocess
import argparse
import re
import json
import string
import xattr
import errno
import tempfile
import csv
import shutil
import collections
import hashlib
import fnmatch
import platform
import logging
import logging.handlers
import textwrap

from typing import *

from enum import Enum

import zeroconf

PY3 = sys.version_info.major >= 3

if PY3:
    from urllib.request import urlopen
    from urllib.parse import urlparse
    from urllib.parse import urljoin
    from urllib.parse import urlunparse
    from urllib.parse import urlencode
    from urllib.parse import quote as urllib_quote
    from urllib.parse import unquote as urllib_unquote
    from urllib.parse import quote_plus as urllib_quote_plus
    from urllib.error import HTTPError
    from urllib.error import URLError
