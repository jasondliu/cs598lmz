import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
# Import the modules we need
#

import sys
import os
import re
import argparse
import pprint
import json
import time
import datetime
import traceback
import urllib
import urllib2
import urlparse
import logging

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin

#
# Globals
#

__addon__       = xbmcaddon.Addon()
__addonid__     = __addon__.getAddonInfo('id')
__addonname__   = __addon__.getAddonInfo('name')
__author__      = __addon__.getAddonInfo('author')
__version__     = __addon__.getAddonInfo('version')
__language__    = __addon__.getLocalizedString
__path__        = __addon__.getAddonInfo('path')
__cwd__         = __addon__.getAddonInfo('path')
__profile__     = __addon__.getAddonInfo('profile
