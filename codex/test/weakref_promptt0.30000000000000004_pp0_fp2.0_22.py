import weakref
# Test weakref.ref(x) is x
assert weakref.ref(1)() == 1
assert weakref.ref(1.0)() == 1.0
assert weakref.ref(1+2j)() == 1+2j
assert weakref.ref('a')() == 'a'
assert weakref.ref(u'a')() == u'a'
assert weakref.ref(True)() is True
assert weakref.ref(False)() is False
assert weakref.ref(None)() is None
assert weakref.ref(object())() is not None
assert weakref.ref(object())() is not None
assert weakref.ref(object())() is not None
assert weakref.ref(object())() is not None
assert weakref.ref(object())() is not None
assert weakref.ref(object())() is not None
assert weakref.ref(object())() is not None
assert weakref.ref(object())() is not None
assert weakref.ref(object())() is not None
assert weakref.ref(object())() is not None
