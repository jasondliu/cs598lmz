import weakref
# Test weakref.ref to function
def function():
    print("function() was called")

func_wrapper = weakref.ref(function)
print(func_wrapper)
function()

del function
print(func_wrapper)
try:
    func_wrapper()
except Exception as e:
    print("Call func_wrapper() failed")
    print("The reason is: ", e)

class A:
    def __init__(self, val):  # Construct an object
        self.val = val

    def hi(self):  # When an object is dead, all its methods are dead too
        print("HI, I'm A,value is ", self.val)

b = A(10)
a_wrapper = weakref.ref(b)
b.hi()
print("a_wrapper is :", a_wrapper)

del b
print("a_wrapper is :", a_wrapper)
try:
    a_wrapper().hi()
except Exception as e:
    print("Call a_wrapper() failed")
    print("The reason is: ", e)


