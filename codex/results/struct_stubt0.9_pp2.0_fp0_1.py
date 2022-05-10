from _struct import Struct
s = Struct.__new__(Struct)
have_unicode = 0
if Msg is not None: 
 _keys = Msg._keys:
 _values = Msg._values:
 _defaults = Msg._defaults:
 _types = Msg._types:
for k in _keys:
 exec "%s=_values[k]" % k
 del k
 if __name__ != "__main__":
 globs[name]=Msg
