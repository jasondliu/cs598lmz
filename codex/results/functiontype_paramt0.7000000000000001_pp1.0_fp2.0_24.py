from types import FunctionType
list(FunctionType(lambda x : x+1, globals(), 'lambda_func') for x in range(10))

# %%
# 不带参数的函数
def f():
    print('without args')

# 带参数的函数
def f_with_args(a, b):
    print('with args', a, b)

def f_with_default_value(a=1, b=1):
    print('with default', a, b)

def f_with_default_value_and_args(a=1, b=1, *args):
    print('with default and args', a, b, args)

def f_with_keyword_arguments(**kwargs):
    print('with kwargs', kwargs)

def f_with_args_and_kwargs(a, b, *args, **kwargs):
    print('with args and kwargs', a, b, args, kwargs)

# %%
# 关于可变参
