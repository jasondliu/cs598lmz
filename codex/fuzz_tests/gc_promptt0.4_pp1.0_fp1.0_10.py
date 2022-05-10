import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class MyClass:
    pass

class MyClass2:
    pass

def test():
    obj = MyClass()
    obj2 = MyClass2()
    obj3 = MyClass()
    obj4 = MyClass2()
    obj5 = MyClass()
    obj6 = MyClass2()
    obj7 = MyClass()
    obj8 = MyClass2()
    obj9 = MyClass()
    obj10 = MyClass2()
    obj11 = MyClass()
    obj12 = MyClass2()
    obj13 = MyClass()
    obj14 = MyClass2()
    obj15 = MyClass()
    obj16 = MyClass2()
    obj17 = MyClass()
    obj18 = MyClass2()
    obj19 = MyClass()
    obj20 = MyClass2()
    obj21 = MyClass()
    obj22 = MyClass2()
    obj23 = MyClass()
    obj24 = MyClass2()
    obj25 = MyClass()
    obj26 = MyClass2()
    obj27 = MyClass()
    obj
