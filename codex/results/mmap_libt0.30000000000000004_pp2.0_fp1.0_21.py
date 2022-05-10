import mmap
import os
import re
import shutil
import sys
import tempfile
import time
import traceback
import urllib
import urllib2
import urlparse

import gdata.youtube
import gdata.youtube.service
import gdata.media
import gdata.geo

# Import the Google API Python Client library
import apiclient
import apiclient.discovery
import apiclient.errors
import apiclient.http
import httplib2
import oauth2client.client
import oauth2client.file
import oauth2client.tools

import config
import common
import youtube

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using O
