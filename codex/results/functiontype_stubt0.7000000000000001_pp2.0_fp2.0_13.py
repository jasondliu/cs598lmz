from types import FunctionType
a = (x for x in [1])
a

dir(a)

dir(next)

next.__name__

next.__code__

next.__code__.co_varnames

next.__code__.co_argcount

next.__code__.co_consts

next.__code__.co_code

next.__defaults__

next.__globals__

next.__closure__

next.__dict__

next.__doc__


## 反射

a = {'name':'alex','age':18}

# getattr
# a.name
# getattr(a,'name')

# setattr
# a.name = 'alex'
# setattr(a,'name','alex')

# hasattr
# hasattr(a,'name')

# delattr
# a.name
# delattr(a,'name')
# a.name

## 模块导入

# import module
# module.function

# import module as m
# import
