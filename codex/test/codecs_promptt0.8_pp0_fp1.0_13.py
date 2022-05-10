import codecs
# Test codecs.register_error( 'my_error', MyError )
from codecs import register_error


class MyError( Exception ):
	"""
	"""
	# By default, this will convert to U+FFFD.
	def __init__( self, code, reason ):
		self.msg = 'My error %s occurs at code 0x%x' % ( reason, code )
		self.code = code
		self.reason = reason

	def __str__( self ):
		return self.msg


def my_error_handler( error ):
	if isinstance( error, UnicodeDecodeError ):
		#print( 'UnicodeDecodeError', error )
		raise MyError( error.object[ error.start ], "invalid character" )
	elif isinstance( error, UnicodeEncodeError ):
		#print( 'UnicodeEncodeError', error )
		raise MyError( ord( error.object[ error.start ] ), "invalid character" )
	else:
		raise error


