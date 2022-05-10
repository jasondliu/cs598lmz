import gc, weakref, sys

def show_all_refs():
	"Show all reachable Python objects. Adapted from http://mail.python.org/pipermail/python-list/2003-February/180315.html"
	for obj in gc.get_objects():
		if isinstance(obj, weakref.ReferenceType):
			obj = obj()
		if obj is not None:
			print obj
			print '\n', sys.getrefcount(obj), 'references\n'

# vim:noet:ts=4:sw=4
