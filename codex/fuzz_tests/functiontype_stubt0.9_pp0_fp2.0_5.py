from types import FunctionType
a = (x for x in [1])
# setattr(a, '__iter__', FunctionType(lambda: 0, a))
# # print(a.__name__)

dict['stu'] = 'data'
print(type(dict))
