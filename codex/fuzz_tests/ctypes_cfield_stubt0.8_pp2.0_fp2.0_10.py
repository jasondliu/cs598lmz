import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
  
class MyDynamicClass(type):

    def __new__(cls, name, bases, attributes):
        attributes['dynamic_attribute'] = 42
        fields = []
        for key,value in attributes.iteritems():
            if isinstance(value, ctypes.CField):
                fields.append((key, value))
                del attributes[key]
        attributes['_fields_'] = fields
        return super(MyDynamicClass, cls).__new__(cls, name, bases, attributes)

cls = MyDynamicClass('S2', (S, ), {})
</code>
The <code>S</code> structure is used as an example of structure without <code>_fields_</code>.
Not tested, but I think it should work.

