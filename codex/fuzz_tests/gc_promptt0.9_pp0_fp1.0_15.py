import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect on weakrefs with callbacks


class Test(object):

    def __del__(self):
        pass


def callback(ref):
    global weakref_was_deleted
    weakref_was_deleted = True


def test():
    # A leaky cycle, creates a chain of:
    #   list -> ... -> () ->
    #                       list -> ...
    lst = []
    lst.append(lst)
    lst = lst[0]
    a = Test()
    b = Test()
    a.b = b
    b.a = a
    lst.append(a)
    wr = weakref.ref(b, callback)
    wr_a = weakref.ref(a)
    del a
    del b
    gc.collect()
    if gc.garbage:
        print('Test failed')
    else:
        print('Test passed')
        return 0


if __name__ == '__main__':
    import sys
    result = test()
    sys.exit(result)
