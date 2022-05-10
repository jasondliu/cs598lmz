import weakref
# Test weakref.ref() and weakref.proxy() with various kinds of objects.


class MyObject:

    def __init__(self, name):
        self.name = name
    self.__dict__


class MyObject2(weakref.finalize, MyObject):

    def __init__(self, name, flag):
        self.flag = flag
        MyObject.__init__(self, name)
        weakref.finalize.__init__(self, self, MyObject2._cleanup,
            name, flag)

    def _cleanup(name, flag):
        pass


class MyObject3(MyObject2):

    def __init__(self, name, flag, flag2):
        self.flag2 = flag2
        MyObject2.__init__(self, name, flag)


class MyObjectN(MyObject):

    def __init__(self, *args):
        self.args = args


def _check_object(obj, classobj, *args, **kwargs):
    print("testing obj = %r, repr = %r, type = %
