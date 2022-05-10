import _struct
# Test _struct.Struct.__new__(self, format)
with self_exc(TypeError, "cannot create '_struct.Struct' instances"):
    _struct.Struct.__new__(_struct.Struct, 'a')


# OrderedDict tests
from collections import OrderedDict
od = OrderedDict()

if sys.version_info < (2, 7):
    with self_exc(AttributeError, "has no attribute 'viewitems'"):
        od.viewitems()
    with self_exc(AttributeError, "has no attribute 'viewkeys'"):
        od.viewkeys()
    with self_exc(AttributeError, "has no attribute 'viewvalues'"):
        od.viewvalues()

od.pop(1)
with self_exc(KeyError):
    od.popitem(1)

from decimal import Decimal
d = Decimal('1.2')
with self_exc(TypeError,
              "'>' not supported between instances of 'Decimal' and 'str'"):
    d > '1'

with self_exc(TypeError,
              "'
