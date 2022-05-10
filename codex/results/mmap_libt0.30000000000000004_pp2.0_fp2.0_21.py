import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from BeautifulSoup import BeautifulSoup

from lib import common
from lib import config
from lib import db
from lib import emailer
from lib import html_utils
from lib import http_utils
from lib import log
from lib import process_utils
from lib import utils
from lib import xbmc_utils

logger = log.get_logger()

def get_video_url(url):
    """
    Gets the video url from the given url.
    """
    logger.debug('Getting video url: %s', url)
    video_url = None
    try:
        video_url = _get_video_url(url)
    except:
        logger.error('Error getting video url: %s', url)
        logger.error(traceback.format_exc())
    return video_url

def _get_video_url(url):
    """
    Gets the video url from the given url.
    """
   
