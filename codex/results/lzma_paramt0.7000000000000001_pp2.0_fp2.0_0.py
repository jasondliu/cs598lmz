from lzma import LZMADecompressor
LZMADecompressor.buf_size = 2 * 1024 * 1024

from ctypes import *
import struct

from rl.core.utils import print_exception, log_debug, log_info
from rl.core.lic_utils import LicUtils

class RLPKG(object):
	
	def __init__(self, file_path, f_open=None, f_write=None, f_read=None, f_close=None):
		
		self._file_path = file_path
		
		self._file_header = None
		self._chunk_headers = []
		self._chunk_dict = {}
		self._decompressor = None
		
		self._f_open = f_open
		self._f_write = f_write
		self._f_read = f_read
		self._f_close = f_close
		
		self._file = None
		
		self._file_size = 0
		
		self.load_package()
	
	
