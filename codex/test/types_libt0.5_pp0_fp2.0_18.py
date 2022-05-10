import types
types.MethodType(lambda self, v: self.__setattr__('_%s' % k, v), None, cls)

def _get_set_property(k, fget=None, fset=None, fdel=None, doc=None):
    return property(
        fget and types.MethodType(fget, None, cls),
        fset and types.MethodType(fset, None, cls),
        fdel and types.MethodType(fdel, None, cls),
        doc)

def _get_set_property_ro(k, fget, doc=None):
    return _get_set_property(k, fget=fget, doc=doc)

def _get_set_property_wo(k, fset, doc=None):
    return _get_set_property(k, fset=fset, doc=doc)

