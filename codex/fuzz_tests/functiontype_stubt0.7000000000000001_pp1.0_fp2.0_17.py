from types import FunctionType
a = (x for x in [1])
b = [1]
print type(a)
print type(b)
print isinstance(a, FunctionType)
print isinstance(b, FunctionType)
for i in a:
    print i

# 列表解析List comprehension
print '列表解析List comprehension'

# 元组Tuple
print '元组Tuple'
tup1 = ();
tup2 = (20);
tup3 = (20,);
print tup1
print tup2
print tup3

# 字典Dictionary
print '字典Dictionary'
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict2 = {'abc': 456}
dict3 = {'abc': 123, 98.6: 37}
print dict1['Name']
print dict1['Age']
print dict2['abc']
print dict3[98.6]

# 集合Set
print '集
