import mmap
import os
import re
import string
import sys
import stat
import struct
import subprocess
import sys
import tempfile
import time

from ocempgui.widgets.Constants import *

from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.internet.utils import getProcessOutput
from twisted.internet.protocol import Protocol, ClientCreator
from twisted.web.client import Agent, HTTPConnectionPool, _GenericHTTPPageGetter, readBody, PartialDownloadError

import config
from utils import *
import utils
import protocol

if config.DEBUG:
	import debug

BODY_SIZE = 1024*1024*16

class FileGhost(Ghost):
	_file = None
	
	def __init__(self, *args):
		Ghost.__init__(self, *args)
	
	def getType(self):
		return 'file'
	
	def getSize(self):
		if self._file:
			return self._file.size
