import types
# Test types.FunctionType
class MyCallable:
    # __call__()
    def __call__(self):
        print("__call__() is called")

# Create instance
c = MyCallable()
c()

print(type(c) == types.FunctionType)

# Now try a different instance
def func():
    pass

print(type(func) == types.FunctionType)
