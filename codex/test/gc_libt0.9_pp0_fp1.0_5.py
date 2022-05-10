import gc, weakref

class Obj:
    def __init__(self):
        print('constructor')

    def __del__(self):
        print('destructor')

# 引用循环
o = Obj()
print(o)
o = 1
print(o)
gc.collect()

class ExpensiveObject:
    def __del__(self):
        print('deleted')

def callback(reference):
    print('callback', reference)

obj = ExpensiveObject()
print(obj)
obj_id = id(obj)

# 引用计数
a = obj
b = obj

print('id a:',id(a))
print('id b:',id(b))

print(b'a')

# weakref.ref(obj, callback)
a = weakref.ref(obj, callback)
# del obj

print(a())
del obj
print(a())

# 弱引用对象
s1 = {1,2,3}

