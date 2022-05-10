import weakref
# Test weakref.ref(str) with a str containing a zero byte.
class C(str):
    pass

C('\0').ref()
C('Hello World!').ref()
