import weakref
# Test weakref.ref()
try:
    weakref.ref(None)
except TypeError:
    pass
else:
    raise RuntimeError

try:
    weakref.ref(1)
except TypeError:
    pass
else:
    raise RuntimeError

try:
    weakref.ref(1.0)
except TypeError:
    pass
else:
    raise RuntimeError

try:
    weakref.ref('1')
except TypeError:
    pass
else:
    raise RuntimeError

try:
    weakref.ref([])
except TypeError:
    pass
else:
    raise RuntimeError

try:
    weakref.ref({})
except TypeError:
    pass
else:
    raise RuntimeError

try:
    weakref.ref(())
except TypeError:
    pass
else:
    raise RuntimeError

try:
    weakref.ref(object())
except TypeError:
    pass
else:
    raise RuntimeError

# Test weakref.proxy()
try:
    weakref.proxy(None)
except Type
