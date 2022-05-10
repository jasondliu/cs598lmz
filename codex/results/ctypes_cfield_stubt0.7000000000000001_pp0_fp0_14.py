import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
However, it's not clear that this is the right name.  Should it be <code>CField</code> or <code>CFieldDescriptor</code> or <code>CField_Descriptor</code> or something else?  Should there be a subtype for types with default values?
The main question is whether this could or should be part of the public API.  If so, what should it be called?


A:

I don't think there is a good reason to expose this type to public API. It's pretty easy to get the same information with <code>isinstance</code> and <code>getattr(type(structure), '_fields_')</code>.
I could imagine providing a <code>_fields_</code> descriptor, which would return the same information, but that is all.

