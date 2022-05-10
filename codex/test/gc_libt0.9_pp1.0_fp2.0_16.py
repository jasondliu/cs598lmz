import gc, weakref, types

def is_cobj( x ) :
    """return True if `x` is a CObject"""
    return isinstance( x, types.CObject )

###############################
# uncomment this to debug the gc
#
# def is_cpyobj( x ) :
#     """return True if `x` is a python object"""
#     return isinstance( x, object )
#
# class Tracer( object ) :
#     def __init__(self) :
#         self._ids = set()
#
#     def append( self, obj ) :
#         self._ids.add( id(obj) )
#
#     def __call__( self, _obj, *args ) :
#         obj = _obj()
#         if self._ids and id(obj) in self._ids :
#             print obj, is_cobj(obj), is_cpyobj(obj), args
#         else :
#             print '+++', obj, is_cobj(obj), is_cpyobj(obj), args
# gct =
