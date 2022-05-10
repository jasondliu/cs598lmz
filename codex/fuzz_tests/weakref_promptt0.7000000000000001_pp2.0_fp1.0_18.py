import weakref
# Test weakref.ref(None)
assert weakref.ref(None)() is None
# Test weakref.ref(30)
assert weakref.ref(30)() == 30
# Test weakref.ref("hello")
assert weakref.ref("hello")() == "hello"
# Test weakref.ref(b"hello")
assert weakref.ref(b"hello")() == b"hello"
# Test weakref.ref((1, "hello"))
assert weakref.ref((1, "hello"))() == (1, "hello")
# Test weakref.ref([1, "hello"])
assert weakref.ref([1, "hello"])() == [1, "hello"]
# Test weakref.ref({1, "hello"})
assert weakref.ref({1, "hello"})() == {1, "hello"}
# Test weakref.ref({"a": 1, "b": "hello"})
assert weakref.ref({"a": 1, "b": "hello"})() == {"a": 1, "b": "hello"}


# Test weakref.getweakref
