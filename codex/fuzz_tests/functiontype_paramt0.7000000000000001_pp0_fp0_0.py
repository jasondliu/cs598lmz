from types import FunctionType
list(FunctionType(f.__code__))
 

#f.__code__.co_code


#def f():
#    return
#
#from types import FunctionType
#list(FunctionType(f.__code__))


#from dis import dis
#dis(f)
#
#def f():
#    return
#
#print(f.__code__.co_code)
#
#from dis import dis
#dis(f)
#
#dis('if True: print(42)')
#
#
#def f(x):
#    x = 2
#    a = x / 2
#    return a
#
#dis(f)
#
#
#def f(x):
#    x = 2
#    a = x / 2
#    return a
#
#from types import FunctionType
#for i in FunctionType(f.__code__).__code__.co_code:
#    print(i)
#
#
#from dis import dis
#
#def f(x):
#    x = 2
#    a
