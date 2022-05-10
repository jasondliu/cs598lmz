import mmap
import os
import re
import sys
import tempfile
import time
import traceback
import urllib
import urllib2
import urlparse
import xml.dom.minidom
import xml.etree.ElementTree

from collections import defaultdict
from datetime import datetime, timedelta
from functools import partial
from itertools import chain
from operator import itemgetter
from optparse import OptionParser
from os.path import basename, dirname, exists, expanduser, isdir, isfile, join
from random import randint
from subprocess import Popen, PIPE
from threading import Thread
from time import sleep
from xml.etree.ElementTree import Element, SubElement

from bs4 import BeautifulSoup
from bs4.element import NavigableString
from dateutil.parser import parse as parse_date
from dateutil.tz import tzlocal
from dateutil.tz import tzutc
from dateutil.tz import tzoffset
from dateutil.tz import tzstr
from dateutil.tz import tzwinlocal
from dateutil.
