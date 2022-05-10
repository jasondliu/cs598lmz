import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def _pack_into(self, obj, offset, space):
        value = getattr(obj, self.name)
        if space.config.translation.tagcachetag:
            w_value = space.wrap(value)
            w_base, w_offs = space.unwrap(space.call_method(w_value, '__tagcache__'))
            base = rffi.cast(rffi.INT, w_base)
            offset = rffi.cast(rffi.INT, w_offs)
            rffi.cast(rffi.VOIDP, obj)[offset] = base
        else:
            rffi.cast(rffi.VOIDP, obj)[offset] = value

class CType(ctypes.CType):
    def _pack_into(self, obj, offset, space):
        if isinstance(self, ctypes.CField):
            c_field = self
        else:
            c_field = CField(self.name, self
