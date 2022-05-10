import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def get_api():
    from . import _rawffi
    return _rawffi.api

@func_renamer(prefix='lltype_')
class GcStruct(object):
    _alloc_flavor_ = 'gc'
    _gckind_ = 'gc'
    _is_varsize_ = False

    def __init__(self, **entries):
        object.__setattr__(self, '_storage', entries)
        if hasattr(self, '_gckind_'):
            if self._gckind_ == 'gc':
                GCStruct.__init__(self)
            elif self._gckind_ == 'raw':
                RawStruct.__init__(self)
            else:
                raise ValueError("unknown _gckind_: %r" % (self._gckind_,))

    def __setattr__(self, name, value):
        object.__getattribute__(self, '_storage')[name] = value

    def __getattr__(self, name):

