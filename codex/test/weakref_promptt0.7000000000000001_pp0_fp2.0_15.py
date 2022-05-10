import weakref
# Test weakref.ref(0)
with pytest.raises(TypeError):
    weakref.ref(0)

# Test weakref.proxy(0)
with pytest.raises(TypeError):
    weakref.proxy(0)
