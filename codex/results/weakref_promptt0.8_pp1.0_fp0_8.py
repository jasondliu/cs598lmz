import weakref
# Test weakref.ref(object)

# class Foo:
#     pass

# o = Foo()

# def show(r):
#     print(r.__weakref__.data)

# r = weakref.ref(o)
# show(r)

# o = None
# show(r)
# o = Foo()
# show(r)

# Test weakref.WeakValueDictionary()

# import weakref
# class Foo:
#     pass

# o = Foo()
# d = weakref.WeakValueDictionary()
# d["foo"] = o

# print(d["foo"])
# print(d.get("bar"))
# print(d.has_key("foo"))
# d.clear()
# print(d.get("foo"))

# Test weakref.ref()

# import weakref
# class Foo:
#     pass

# o = Foo()

# def show(r):
#     print(r.__weakref__.data)

# r = weakref.ref(o)
# show(
