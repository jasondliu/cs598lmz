import weakref
# Test weakref.ref
class C:
    pass
obj = C()
print(o)
r = weakref.ref(o)
print(r())

# 循环的断言
# del o  
# print(r())

print('^' * 10)

# Test weakref.WeakValueDictionary
class D:
    pass

d = D()

mapping = {}
mapping[1] = d
print(mapping[1])

weak_key_dict = weakref.WeakValueDictionary()
weak_key_dict[10] = d
print(weak_key_dict[10])
