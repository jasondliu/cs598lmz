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

from optparse import OptionParser

# This is the default location for the 'update.py' script.
UPDATE_URL = 'https://raw.github.com/mozilla/mozmill-ci/master/scripts/update.py'

# This is the default location for the 'mozmill-automation' repository.
MOZMILL_AUTOMATION_URL = 'https://github.com/mozilla/mozmill-automation.git'

# This is the default location for the 'mozmill-automation' repository.
MOZMILL_AUTOMATION_BRANCH = 'master'

# This is the default location for the 'mozmill-automation' repository.
MOZMILL_AUTOMATION_DIR = 'mozmill-automation'

# This is the default location for the 'mozmill-automation' repository.
MOZMILL_
