import ctypes
ctypes.cast(id(int), ctypes.py_object).value

#from functools import reduce
#
#def my_reduce(func,seq):
#    result = seq[0]
#    for i in seq[1:]:
#        result = func(result,i)
#    return result
#
#def sum(x,y):
#    return x+y
#
#print(my_reduce(sum,[1,2,3,4,5]))

#def log(func):
#    def wrapper(*args,**kw):
#        print('call %s():'% func.__name__)
#        return func(*args,**kw)
#    return wrapper
#
#@log
#def now():
#    print('2015-3-25')
#
#now()

#from functools import reduce
#
#def str2num(s):
#    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7
