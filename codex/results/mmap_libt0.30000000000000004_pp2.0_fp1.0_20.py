import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import urllib
import urllib2
import urlparse
import xml.etree.ElementTree as ET

try:
    import json
except ImportError:
    import simplejson as json

try:
    import cPickle as pickle
except ImportError:
    import pickle

try:
    from PIL import Image
except ImportError:
    Image = None

try:
    import pyexiv2
except ImportError:
    pyexiv2 = None

try:
    from scipy.misc import imsave
except ImportError:
    imsave = None

try:
    import pycurl
except ImportError:
    pycurl = None

try:
    import pycurl_manager
except ImportError:
    pycurl_manager = None

try:
    import requests
except ImportError:
    requests = None

try:
    import requests_manager
except ImportError:
    requests_manager =
