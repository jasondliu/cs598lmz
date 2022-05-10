import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse
import xml.dom.minidom
import zipfile
import zlib

from optparse import OptionParser

import buildbot
import buildbot.locks
import buildbot.process.buildstep
import buildbot.process.properties
import buildbot.process.results
import buildbot.reporters.mail
import buildbot.steps.shell
import buildbot.util.service
import buildbot.worker.local

from twisted.internet import defer, reactor, task
from twisted.python import log
from twisted.web import server, static
from twisted.web.resource import Resource
from twisted.web.util import Redirect

from buildbot.status.web.base import HtmlResource, path_to_authzfail
from buildbot.status.web.base import path_to_authzfail, path_to_root, path_to_authzok
from buildbot.status.web.base import path_to_root, path_to_authzok
from build
