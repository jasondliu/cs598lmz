import gc, weakref

def f(obj):
    # 在这里引用对象
    print('obj:', obj)

obj = C()
r = weakref.ref(obj, f)

# 输出: obj: <__main__.C object at 0x10e100070>
print('obj:', obj)

del obj
# 输出: obj: None
print('obj:', r())

# 输出: obj: None
print('obj:', r())
