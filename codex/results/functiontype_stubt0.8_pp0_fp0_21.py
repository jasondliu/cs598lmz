from types import FunctionType
a = (x for x in [1])
print( isinstance(a, GeneratorType))


#变量
a = 123
a = "hello"
#引用
a = b = [-1]
#复合赋值
a = 2
a+=3
a = a+3

a, b = 1, "hello"
a, b = b, a

#字符串不可变
a = "hello world"
#a[0] = 'c' error

#字符串格式化 % 格式字符
a = '%s you are so %s' % ('hello', "good")
print(a)
# format
a = "hello {name}, you are so {how}"
a = a.format(name="world", how="good")
print(a)

#字符串处理

a = "hello world"
b = "hell"

#判断子串位置
print( a.
