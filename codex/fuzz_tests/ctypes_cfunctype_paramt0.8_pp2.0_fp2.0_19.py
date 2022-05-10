import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.py_object, ctypes.c_void_p, ctypes.py_object )

# utility function to extract an attribute from a python object
# usage: attr = getAttr( obj, attr )
def getAttr( obj, strAttr ):
	# get the descriptor
	attr = obj.__class__.__dict__[strAttr]
	# check it is a data descriptor
	if hasattr( attr, '__get__' ):
		return attr.__get__( obj, obj.__class__ )
	else:
		return attr

# utility function to set an attribute of a python object
# usage: setAttr( obj, attr, value )
def setAttr( obj, attr, value ):
	# get the descriptor
	desc = obj.__class__.__dict__[attr]
	# check it is a data descriptor
	if hasattr( desc, '__set__' ):
		desc.__set__( obj, value )
	else:
		obj.__dict__[attr]
