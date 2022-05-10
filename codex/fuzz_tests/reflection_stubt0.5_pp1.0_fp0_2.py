fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_closures
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add5 = make_adder(5)
add5(10)

# test_classes
class A:
    pass

a = A()
a.x = 5
a.x

# test_class_attributes
class A:
    x = 5

a = A()
a.x

# test_class_attributes_2
class A:
    x = 5

A.x

# test_class_attributes_3
class A:
    x = 5

A.x = 7
A.x

# test_class_attributes_4
class A:
    x = 5

a = A()
a.x = 7
a.x

# test_class_attributes_5
class A:
    x = 5

b = A()
A.x = 7
b.x

# test_class_attributes_6
class A
