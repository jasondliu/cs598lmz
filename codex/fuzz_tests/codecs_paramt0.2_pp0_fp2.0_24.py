import codecs
codecs.register_error('strict', codecs.ignore_errors)

# The following is a hack to make sure that the "en" module is loaded
# before we try to use it.
import gettext
gettext.NullTranslations().ugettext

import os
import sys
import locale
import logging
import logging.handlers
import traceback
import warnings
import signal
import optparse

from miro import app
from miro import prefs
from miro import fileutil
from miro import util
from miro import eventloop
from miro import messages
from miro import startup
from miro import autoupdate
from miro import httpauth
from miro import singleclick
from miro import commandline
from miro import databaseupgrade
from miro import database
from miro import filetypes
from miro import item
from miro import feed
from miro import guide
from miro import folder
from miro import playlist
from miro import itemtrack
from miro import metadata
from miro import searchengines
from miro import search
from miro import devices
from miro import device
from m
