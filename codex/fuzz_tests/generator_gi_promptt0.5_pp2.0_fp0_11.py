gi = (i for i in ())
# Test gi.gi_code.co_name
print(type(gi.gi_code.co_name))

# Test tp_dictoffset
class A(object):
    pass

# Test tp_dictoffset
A.__dict__

# Test tp_dictoffset
class B(A):
    pass

# Test tp_dictoffset
B.__dict__

# Test tp_dictoffset
class C(object):
    pass

# Test tp_dictoffset
C.__dict__

# Test tp_dictoffset
class D(C):
    pass

# Test tp_dictoffset
D.__dict__

# Test tp_dictoffset
class E(C):
    pass

# Test tp_dictoffset
E.__dict__

# Test tp_dictoffset
class F(C):
    pass

# Test tp_dictoffset
F.__dict__

# Test tp_dictoffset
class G(C):
    pass

# Test tp_dictoffset
G.__dict__

# Test t
