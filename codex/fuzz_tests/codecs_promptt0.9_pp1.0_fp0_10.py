import codecs
# Test codecs.register_error('custom', custom_error_function)
import logging
import os
import random
import socket
import subprocess
import sys
import time
import urllib
import urllib2

# To test urllib.quote() and urllib.unquote().

# Get a global logger.
logger = logging.getLogger()

# The filepath to the directory of this script:
this_filepath = os.path.dirname(__file__)

# Get this script's name without the ".py"
thisfilename = os.path.basename(__file__)[:-len('.py')]

# This script's sf.net project id, which is
# used when updating the version number in
# "github_authorisation_data.py"
PROJECT_ID = ''

# Get PID
pid = os.getpid()

KEYCHAIN_NAME = 'github_authorisation_data.py'

# The username in the keychain file.
github_username = ''

# The GitHub password (an access token) in the keychain file.

