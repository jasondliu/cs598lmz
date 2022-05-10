import types
# Test types.FunctionType
def test_types_FunctionType(x):
    type_of_x = type(x)
    if type_of_x == types.FunctionType:
        print("x is a function")
    else:
        print("x is not a function")

def test_types_FunctionType_with_lambda(x):
    type_of_x = type(x)
    if type_of_x == types.FunctionType:
        print("x is a function")
    else:
        print("x is not a function")

# Test types.LambdaType
def test_types_LambdaType(x):
    type_of_x = type(x)
    if type_of_x == types.LambdaType:
        print("x is a lambda function")
    else:
        print("x is not a lambda function")

def test_types_LambdaType_with_lambda(x):
    type_of_x = type(x)
    if type_of_x == types.LambdaType:
        print("x is a lambda
