import weakref
# Test weakref.ref()
ref = weakref.ref(None)

if ref() is None:
    print('ok')

# Test weakref.WeakValueDictionary
class Test:
    pass

obj = Test()

dict = weakref.WeakValueDictionary()
dict[obj] = 1

li = []
for i in dict:
    li.append(i)

if li == [obj]:
    print('ok')

# Test weakref.ref()
ref = weakref.ref(None)

if ref() is None:
    print('ok')

# Test weakref.WeakValueDictionary
class Test:
    pass

obj = Test()

dict = weakref.WeakValueDictionary()
dict[obj] = 1

li = []
for i in dict:
    li.append(i)

if li == [obj]:
    print('ok')
