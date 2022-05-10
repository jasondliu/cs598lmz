from types import FunctionType
a = (x for x in [1])
print(type(a))

print(type(lambda x: x))

print(type(FunctionType))

print(type(type))

print(type(type(type)))



# 过滤列表中的空元素

s = ["a", "", "b", "", "  "]
print(list(filter(None, s)))


# 取消列表中的重复元素

s = ["a", "b", "a", "b", "c"]
print(list(set(s)))


# 字符串首字母大写

s = "hello world"
print(s.capitalize())

# 字符串首字母小写

s = "Hello World"
print(s.lower())

# 字符串中每个单词首字母
