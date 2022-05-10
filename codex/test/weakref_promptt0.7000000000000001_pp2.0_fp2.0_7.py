import weakref
# Test weakref.ref(type(1))
# with pytest.raises(TypeError):
#     weakref.ref(type(1))
# del weakref

# Test weakref.ref(type)
# with pytest.raises(TypeError):
#     weakref.ref(type)
# del weakref

# Test weakref.ref(str)
# with pytest.raises(TypeError):
#     weakref.ref(str)
# del weakref

# Test weakref.ref(object)
# with pytest.raises(TypeError):
#     weakref.ref(object)
# del weakref

# Test for issue#11067
class A:
    pass

# with pytest.raises(TypeError):
#     A.__weakref__ = 2
# del A

# Test for issue#11116
class A:
    pass

# with pytest.raises(TypeError):
#     A.__dict__ = 2
# del A

# Test for issue#11115
# with pytest.raises(TypeError
