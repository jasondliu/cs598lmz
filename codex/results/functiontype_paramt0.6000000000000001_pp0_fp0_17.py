from types import FunctionType
list(FunctionType(f.__code__, globals(), 'lambda_name', f.__defaults__, f.__closure__))

#%%
#builtin Functions
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#%%
#builtin Functions
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#%%
#builtin Functions
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#%%
#builtin Functions
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad
