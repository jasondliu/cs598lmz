import types
# Test types.FunctionType
# Syntax: types.FunctionType(object, object, object)
def functionType(object, object1, object2):
    print(type(object))
    print(type(object1))
    print(type(object2))


# Test types.LambdaType
# Syntax: types.LambdaType(object, object, object)
def lambdaType(object, object1, object2):
    print (type(object))
    print (type(object1))
    print (type(object2))


# Test types.GeneratorType
# Syntax: types.GeneratorType(object)
def generatorType(object):
    print (type(object))


# Test types.CodeType
# Syntax: types.CodeType(object, object, object, object, object,
#                        object, object, object, object, object,
#                        object, object, object)
def codeType(object, object1, object2, object3, object4, object5,
             object6, object7, object8, object9, object10, object11,
             object12
