import gc, weakref

from . import _util as util

#===============================================================================
#																				#
#																				#
#																				#
#																				#
#																				#
#===============================================================================

class _Base(object):
	"""
	Base class for all objects in the library.
	
	This class provides a number of useful functions that are needed by all
	objects in the library.
	"""
	
	#---------------------------------------------------------------------------
	#																		   #
	#																		   #
	#															
