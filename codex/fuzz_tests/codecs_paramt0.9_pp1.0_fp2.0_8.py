import codecs
codecs.register_error("strict", codecs.ignore_errors)

# Set default encoding to utf-8, the only encoding that makes sense when dealing with the interne
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Logger(object):
	""" A simple wrapper around python's logging module, providing some defaults and uniform call """
	def __init__(self):
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		
		# Add handler:
		handler = logging.StreamHandler(sys.stdout)
		formatter = logging.Formatter('[%(levelname)s] %(name)s - %(message)s')
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)
	
	def debug(self, msg):
		self.logger.debug(msg)
	
	def info(self, msg):
		self.logger.info(msg)
	
	def warning(
