from types import FunctionType
a = (x for x in [1]) #generator
a.__next__()

#使用断言语句来判断条件是否正确
assert True
assert 1 == 1
assert 'a' in ['a']
assert [1]
#assert [] #AssertionError: []

#断言语句可以接受一个可选的错误信息，assert 后面的语句不会被执行，所以后面的语句可以不用在assert后面加括号
assert 1 == 0, '1不等于0'
#assert 1 == 0, b #b未定义，所以这条语句不会被执行

#可迭代对象：iterable
