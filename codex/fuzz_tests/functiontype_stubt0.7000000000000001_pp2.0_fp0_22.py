from types import FunctionType
a = (x for x in [1])
print(isinstance(a, (list, tuple)))
print(isinstance(a, (list, tuple, GeneratorType)))
print(isinstance(a, (GeneratorType, )))

print(isinstance(a, FunctionType))
print(isinstance(a, (list, tuple, GeneratorType, FunctionType)))

try:
    b = (1)
    print(isinstance(b, (list, tuple, GeneratorType, FunctionType)))
except Exception as e:
    print(e)

# 这里有点坑,后面改为False
print(isinstance(b, (list, tuple, GeneratorType, FunctionType, type(None))))
# 这里不是type(None),所以上面的都不算
print(type(None))

# 总结,元组不算,type(None) 算None,其他的类型都算
