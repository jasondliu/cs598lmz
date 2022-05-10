import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import sys
import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from math import ceil
from optparse import OptionParser
import time
import json
from urllib import quote
import urllib2
from urllib2 import HTTPError, URLError
import httplib
import socket
import os
import re
import random
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler
import signal
from threading import Thread
import threading
import Queue
from Queue import Queue
import traceback
import glob
import sqlite3
from sqlite3 import OperationalError
import subprocess
import pwd
import grp
from collections import defaultdict
from collections import OrderedDict
import ConfigParser
import inspect
from inspect import getmembers
import pprint
import gzip
import shutil
import zipfile
from zipfile import ZipFile, ZIP_
