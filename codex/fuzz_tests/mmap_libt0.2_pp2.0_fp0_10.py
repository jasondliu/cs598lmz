import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import xbmcvfs
import xbmcgui
import xbmc

from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from datetime import date
from dateutil import parser
from dateutil import tz
from dateutil.relativedelta import relativedelta
from HTMLParser import HTMLParser
from HTMLParser import HTMLParseError
from StringIO import StringIO
from threading import Thread
from threading import Timer
from xml.dom.minidom import parseString

from resources.lib.globals import *
from resources.lib.globals import log as log
from resources.lib.globals import settings as settings
from resources.lib.globals import utils as utils
from resources.lib.globals import variables as variables
from resources.lib.globals import xbmc_
