import ctypes

class S(ctypes.Structure):
    x = ctypes.CFUNCTYPE(NONE)
    _fields_ = [x]
S().x
S()._fields_[0] = ctypes.CFUNCTYPE(NONE) # infinite recursion!
</code>
I guess it is possible to test for recursion myself, by comparing fields with types, but I'd prefer if it were handled by the standard library.
Also, I find it strange that the infinite recursion is only a problem with the <code>Structure</code> class, not the <code>Union</code> class.


A:

The <code>_fields_[0]</code> descriptor stores the class in a field member_type, which of course is a <code>type(Structure)</code>. You are replacing member type with itself, hence the infinite recursion.
Here's some code that works around the problem:
<code>def print_field_types(field_type):
    print 'cant print {}'.format(field_type)
    for (_, field_sub_type) in field_type._fields_:
        if field_sub_type ==
