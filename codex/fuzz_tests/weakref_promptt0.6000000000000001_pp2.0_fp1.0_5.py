import weakref
# Test weakref.ref(return_value)

class A(object):
    def __init__(self):
        self.foo = 'bar'

def wrapper(a):
    return a

def make_ref(a):
    return weakref.ref(a)

def return_value():
    return A()

# CHECK-LABEL: @return_value
# CHECK: %[[REF:.*]] = call %struct.A* @return_value()
# CHECK-NEXT: %[[REF2:.*]] = call %struct.A* @return_value()
# CHECK-NEXT: %[[REF3:.*]] = call %struct.A* @return_value()
# CHECK-NEXT: %[[REF4:.*]] = call %struct.A* @return_value()
# CHECK-NEXT: %[[REF5:.*]] = call %struct.A* @return_value()
# CHECK-NEXT: %[[REF6:.*]] = call %struct.A* @return_value()
# CHECK-NEXT: %[[REF7
