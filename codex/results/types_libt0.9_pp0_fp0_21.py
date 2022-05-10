import types
types.MethodType(lambda self, x : 1, None)

from js.builtins import dict
d = dict()
del d[dict()]

from js.wrappers import W_Array
W_Array.new(20)

from js.object_space import w_None
w_None.to_string()
w_None.to_number()
w_None.to_object()
w_None.call_simple_function()
w_None.descr_getattr()
w_None.descr_setattr()
w_None.get_own_property_names()
w_None.get_own_property_descriptor()
w_None.define_own_property()

from js.builtins import date
date.Date.new(0)
date.Date.call_method('getDate', [date.Date.new(0)])
date.Date.get_property(date.Date.new(0), 'getDate')

from js import debug
debug.debug()
