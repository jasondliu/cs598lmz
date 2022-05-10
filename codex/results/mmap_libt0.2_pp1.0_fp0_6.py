import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse
import xml.etree.ElementTree as ET

from datetime import datetime
from datetime import timedelta
from datetime import tzinfo

from xml.sax.saxutils import escape

from plexapi.exceptions import BadRequest, NotFound
from plexapi.utils import cast
from plexapi.utils import download
from plexapi.utils import getXML
from plexapi.utils import joinArgs
from plexapi.utils import PlexPartialObject
from plexapi.utils import PlexURL
from plexapi.utils import search
from plexapi.utils import toDatetime
from plexapi.utils import update_params
from plexapi.utils import verify_ssl

# Globals
PLEX_HEADERS = {'X-Plex-Platform': 'Python',
                'X-Plex-Platform-Version': sys.version.split()[0],
                'X-Plex-Provides': 'player',
                '
