import types
types.DictType = dict
types.StringTypes = str,
types.ListType = list

try:
    import ujson as json
except ImportError:
    import json

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse

import requests

from . import users as usr
from . import organization as org
from . import project as proj
from . import entry as e
from . import role as r
from . import notification as n
from . import common as c
from . import comment as co
from . import message as m
from . import timeentry as te
from . import timereport as tr
from . import activity as t
from . import availability as av

__all__ = [
    'Users',
    'Organization',
    'Project',
    'Entry',
    'Role',
    'Notification',
    'Comment',
    'Message',
    'TimeEntry',
    'TimeReport',
    'Activity',
    'Availability',
    ]

log = logging.getLogger(__name__)


