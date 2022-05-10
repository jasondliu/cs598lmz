import types
# Test types.FunctionType
print("\nTest types.FunctionType")

def function1():
    print("Function 1")

def function2():
    print("Function 2")

func_dict = {function1: "function1", function2: "function2"}
for func in func_dict:
    if isinstance(func, types.FunctionType):
        print("%s is a function type" % func)
    else:
        print("%s is not a function type" % func)


# Test types.LambdaType
print("\nTest types.LambdaType")

func_dict = {lambda x: x+1: "lambda x: x+1", lambda x, y: x+y: "lambda x, y: x+y"}
for func in func_dict:
    if isinstance(func, types.LambdaType):
        print("%s is a lambda type" % func)
    else:
        print("%s is not a lambda type" % func)


# Test types.GeneratorType
print("\nTest types.GeneratorType")
def
