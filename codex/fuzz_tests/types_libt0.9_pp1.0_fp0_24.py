import types
types.new_class(__name__)
class _attr: v = __name__

__all__ = []

def __repr__(self, level=0):
	tostr = lambda *args: ''.join(str(arg) for arg in args)
	indentation = '\t' * level
	contents = '\n'.join('%s%s\n' % (indentation, tostr(arg)) for arg in self._args)
	return '%s(\n%s\n%s)' % (self.__class__._attr.v, contents, indentation)

def __init__(self, *args):
	for arg in args:
		if type(arg) != type:
			raise TypeError("Argument %s to __init__ is not a type" % str(arg))
	super(self.__class__, self).__init__()
	self._args = args

_attr.v = types.new_class(_attr.v)
_attr.v.__init__ = __init__
_attr.
