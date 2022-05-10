import types
# Test types.FunctionType just to be sure
def myFunction():
    print("Howdy")

if type(myFunction) == types.FunctionType:
    print("myFunction is a function")

if type(myFunction) == types.BuiltinFunctionType:
    print("myFunction is a built-in function")

if type(myFunction) == types.BuiltinMethodType:
    print("myFunction is a built-in method")

# Built-in examples
def test_builtin_types():
    # calling built-in function type
    # In the below case 
    # 1. type is a built in function 
    # 2. list is a built in class 
    # 3. x is an instance of the built in class
    # 4. the type of the instance will be returned 
    x = type(x)
    print(x)

    # calling built-in class list
    x = type(list)
    print(x)

    # calling built-in class list
    x = type(list())
    print(x)

test_builtin_types()

#
