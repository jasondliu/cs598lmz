from types import FunctionType
list(FunctionType(lambda: None).__code__.co_varnames)

# 使用反射
import inspect
inspect.getargspec(lambda: None)

# 使用源码
import ast
def get_args(func):
    return [arg.arg for arg in ast.parse(func.__code__.co_consts[0].co_consts[1].body).body[0].args.args]

get_args(lambda: None)

# 使用源码2
import ast
def get_args(func):
    return [node.id for node in ast.parse(func.__code__.co_consts[0].co_consts[1].body).body[0].args.args]

get_args(lambda: None)

# 使用源码3
import ast
def get_args(func):
    return [node.id for node in ast.parse(func.__code__.co_consts[0].co_consts[1
