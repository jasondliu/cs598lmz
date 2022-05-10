import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import os
import re
import time
import json
import urllib
import urllib2
import urlparse
import logging
import datetime
import collections
import traceback
import random
import socket

from pprint import pprint
from optparse import OptionParser

from xml.dom import minidom
from xml.dom.minidom import parseString

from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup, Tag

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon

import CommonFunctions as common
common.plugin = "plugin.video.dramafever"

from resources.lib import utils
from resources.lib.utils import *
from resources.lib.dramafever import *

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%H:%M:%S',
    filename=os.path
