import types
types.MethodType(lambda self: None, None, Dummy)

# Test for SF bug #1465388
class C:
    def __init__(self):
        self.__super = super(C, self)
        class D(C):
            def __init__(self):
                self.__super.__init__()
        D()

# Test for SF bug #1476645
class C(object):
    def __init__(self):
        super(C, self).__init__()
        class D(C):
            def __init__(self):
                super(D, self).__init__()
        D()

# Test for SF bug #1477347
class C(object):
    def __init__(self):
        super(C, self).__init__()
        class D(C):
            def __init__(self):
                super(D, self).__init__()
        class E(C):
            def __init__(self):
                super(E, self).__init__()
        E()

# Test for SF
