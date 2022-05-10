import gc, weakref

# Globals, mostly for printing

_objectmap = {}
_inversemap = {}
_functions = {}
_voidpointers = {}
_classpointers = {}
_refcount = {}
_structs = {}


# Basic exception type

class FFIError(Exception):
    pass

# Used to record the function name and such

class _CDataMeta(type):

    def __new__(cls, name, bases, dct):
        k = type.__new__(cls, name, bases, dct)
        if '_c_type_' in dct and dct['_c_type_'].startswith('functype('):
            if '_c_name_' in dct:
                _functions[k] = dct['_c_name_']
            else:
                _functions[k] = '<anonymous>'
        return k

_CDataMeta = _CDataMeta('_CDataMeta', (object, ), {})

class _CData(_CDataMeta):

    #_
