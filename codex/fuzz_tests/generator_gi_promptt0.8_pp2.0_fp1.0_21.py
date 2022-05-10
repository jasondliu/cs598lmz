gi = (i for i in ())
# Test gi.gi_code is code of <listcomp>.
listcomp = [x for x in 'ABC']
my_listcomp = [x for x in 'ABC']
my_listcomp.append(4)
print(my_listcomp)

func = lambda x:print(x)

# Test a lambda function.
# print(func(5))
# print(func.__code__.co_varnames)
# print(func.__code__.co_argcount)

# Test a nested function.
# def func():
#     def nester():
#         1 + 1
#     nester()
#
# print(func.__code__.co_consts)
# print(func.__code__.co_varnames)
# print(func.__code__.co_nlocals)

# Test a class.
class Test(object):
    pass

print(Test.__code__.co_varnames)
print(Test.__code__.co_nlocals)

import keyword
print(keyword.kwlist)

# Test a
