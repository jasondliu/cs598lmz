import types
# Test types.FunctionType
def is_function_type(func):
    return type(func) == types.FunctionType

# Test type bound methods
def is_method_type(func):
    return type(func) == types.MethodType

# Test lambdas
def is_lambda_type(func):
    return type(func) == types.LambdaType

def has_arg_with_default(func):
    # import inspect
    # return inspect.getargspec(func).defaults is not None
    # or
    import argparse
    arg_list = argparse.ArgumentParser().parse_args(['foo','bar'])[1:]
    return func(*arg_list)

def has_vararg(func):
    import argparse
    arg_list = argparse.ArgumentParser().parse_args(['foo','bar'])[1:]
    return func(*arg_list)

def has_kwarg(func):
    import argparse
    arg_list = argparse.ArgumentParser().parse_args(['foo','bar'])[1:]
    return
