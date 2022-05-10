import ctypes

class S(ctypes.Structure):
    x = 1

p = ctypes.POINTER(S)()
p.x = 2
print(p.x)   # print 2 and not 1.
</code>
How can I prevent the field <code>x</code> of the <code>Structure</code> instance to be accessed through a pointer?
The reason is that I'm extending the Structure with a custom metaclass, and will add <code>_pointer_fields</code> and <code>_value_fields</code> attributes to the class. The <code>_pointer_fields</code> attribute will contain the list of fields which can be accessed through a pointer, and the <code>_value_fields</code> attribute will contain the fields which can be accessed through a structure instance.
So far I cannot figure out how to implement this.

