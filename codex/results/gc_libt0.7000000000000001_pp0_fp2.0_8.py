import gc, weakref


class Foo(object):
    pass


def callback(obj, x):
    print 'callback: obj: {}, x: {}'.format(obj, x)


def weak_ref_callback(obj):
    print 'weak_ref_callback: callback is dead:', obj() is None


# 设置一个键值对 foo.x = 1
foo = Foo()
foo.x = 1

# 在键 x 上设置弱回调
weakref.add_weakref_callback(foo, callback, foo.x)
# 添加一个弱引用
weak_obj = weakref.ref(foo, weak_ref_callback)

# 手动调用垃圾回收
gc.collect()
# 输出: callback: obj: <__main__.Foo object at 0x10c5bd950>, x: 1

# 删除 foo
