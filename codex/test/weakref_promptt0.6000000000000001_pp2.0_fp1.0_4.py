import weakref
# Test weakref.ref(function)

def get_obj():
    return [1, 2, 3]

def get_function():
    def f():
        pass

    return f

def get_method():
    class C:
        def foo(self):
            pass

    return C().foo

def get_bound_method():
    class C:
        def foo(self):
            pass

    return C().foo

def get_builtin_function():
    return len

def get_builtin_method():
    return len([])

def get_method_descriptor():
    class C:
        foo = 7

    return C.foo

def get_member_descriptor():
    class C:
        foo = 7

    return C.foo

def get_getset_descriptor():
    class C:
        def getx(self):
            return self.__x

        def setx(self, v):
            self.__x = v

        def delx(self):
            del self.__x

