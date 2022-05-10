import codecs
codecs.register_error('strict', codecs.ignore_errors)

import os
import sys
import re
import argparse
import logging
import subprocess
import shutil
import tempfile
import time
import datetime
import json
import urllib
import urllib2
import urlparse
import zipfile
import tarfile
import hashlib
import shutil
import glob
import fnmatch
import xml.etree.ElementTree as ET

import requests

from . import __version__

log = logging.getLogger(__name__)

# ------------------------------------------------------------------------------
#
# Utility functions
#
# ------------------------------------------------------------------------------

def get_platform():
    """
    Returns the platform name.
    """
    platforms = {
        'linux1' : 'linux',
        'linux2' : 'linux',
        'darwin' : 'macosx',
        'win32' : 'windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]

def get_arch():
    """
    Returns the architecture name.
   
