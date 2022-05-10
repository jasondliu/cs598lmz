from _struct import Struct
s = Struct.__new__(Struct)
s.size = 3

def _get_format(self):
    return self._fmt

def _set_format(self, fmt):
    self._fmt = fmt

Struct.format = property(_get_format, _set_format)
</code>
After the monkeypatch, <code>Struct.size</code> is still <code>3</code>, but <code>Struct.format</code> is now a property.

