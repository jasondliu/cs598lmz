import codecs
# Test codecs.register_error for python 3.x
#
#   codecs.register_error(name, handler)
#
# Registers the specified error handler under the name name. handler
# may be a callable that takes a unicode argument and returns a unicode
# object, or a dictionary mapping unicode ordinals to unicode ordinals,
# strings or None. The latter type of mapping is used to implement
# "replace" and "ignore" handlers.

