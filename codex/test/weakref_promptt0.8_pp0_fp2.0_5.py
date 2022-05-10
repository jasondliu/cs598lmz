import weakref
# Test weakref.ref(target, ondelete)
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
def got_it(ref):
    print("got it:", ref)
    return ref
a = A(3)
ref = weakref.ref(a, got_it)
b = A(4)
a = b
# got it: <weakref at 0x7f2b2bf7e198; dead>
print("after replace:", ref)

print("="*20, "<end test2>", "*"*20)
####################################################################################################
import weakref
import gc
def got_it(ref):
    print("got it:", ref)
    return ref
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
a = A(5)
ref = weakref.ref(a, got_it)
