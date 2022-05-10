import types
# Test types.FunctionType and types.MethodType
print('types.FunctionType:', types.FunctionType)
print('types.MethodType:', types.MethodType)

# Test cProfile
import cProfile
def func():
    for i in range(10):
        print(i)
cProfile.run('func()')
