import gc, weakref

def show_refs(obj):
    print('%s is referenced by' % str(obj), end=' ')
    refs = gc.get_referents(obj)
    for ref in refs:
        print(ref, end=' ')
    print()

def test_weakref():
    obj = [1, 2, 3]
    show_refs(obj)
    # 构建弱引用对象
    wref = weakref.ref(obj)
    # 弱引用对象是否有效
    print('obj is valid:', wref() is not None)
    # 删除强引用
    del obj
    print('obj is valid:', wref() is not None)
    gc.collect()
    print('obj is valid:', wref() is not None)

test_weakref()
