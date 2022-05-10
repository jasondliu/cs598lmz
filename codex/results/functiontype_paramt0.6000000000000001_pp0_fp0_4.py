from types import FunctionType
list(FunctionType(code1,globals(),'test'))

# isinstance()  判断一个对象是否是一个已知的类型
# issubclass()  判断参数class是否是classinfo类型的子类
# hasattr()  判断对象是否包含对应的属性
# getattr()  获取对象对应属性的值
# setattr()  设置对象的属性值，如果属性不存在，先创建再设置
# delattr()  删除对象的属性


print(isinstance(test,FunctionType))
print(isinstance(c,A))
print
