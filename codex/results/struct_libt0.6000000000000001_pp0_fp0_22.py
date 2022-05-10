import _struct

import pytz
import tzlocal

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
from datetime import timezone
from datetime import tzinfo

from dateutil import rrule
from dateutil import parser
from dateutil import relativedelta
from dateutil import tz as dateutil_tz

from khal.exceptions import FatalError

from . import __pkginfo__
from .log import logger

import re

try:
    import vdirsyncer.storage.filesystem as vdirsyncer_fs
except ImportError:
    vdirsyncer_fs = None

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

try:
    from configparser import RawConfigParser
except ImportError:
    from ConfigParser import RawConfigParser

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

try:
    from tzlocal import get_localzone

