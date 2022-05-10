import types
types.FunctionType
types.LambdaType
types.MethodType
types.UnboundMethodType


def get_base_types():
    # return a list of all base types
    return [getattr(types, t) for t in dir(types) if not t.endswith("Type")]


def check(obj):
    # check if obj is of any of the types in the argument 'types'
    for t in get_base_types():
        if isinstance(obj, t):
            return True
    return False


def is_method(obj):
    # check if obj is a method
    return check(obj) and not isinstance(obj, types.LambdaType)


def is_lambda(obj):
    # check if obj is a lambda
    return isinstance(obj, types.LambdaType)


def is_function(obj):
    # check if obj is a function
    return check(obj) and not isinstance(obj, (types.MethodType, types.LambdaType))


#--------------------------------------------------------------------------------------------------------------------
#    TYPES
#----------------------------------------------------------------
