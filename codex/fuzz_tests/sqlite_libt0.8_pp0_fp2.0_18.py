import ctypes
import ctypes.util
import threading
import sqlite3


from lib.clamav import *
from lib.clamav import _libclamav as libclamav

from lib.common import *
from lib.common import _libcommon as libcommon
from lib.common.Constants import *

from lib.core import *
from lib.core import _libcore as libcore
from lib.core.Constants import *
from lib.core.Exceptions import *

class Scanner(object):
	def __init__(self):
		self.loaded = False
		self.engine_version = None
		self._lock = threading.Lock()
		self._libclamav = libclamav
		self._libcommon = libcommon
		self._libcore = libcore

	def load(self, paths=[]):
		if self.engine_version:
			return

		self._libcore.cl_init(CL_INIT_DEFAULT)

		if not paths:
			self._libcommon.cl_initialize_crypto()
			self._
