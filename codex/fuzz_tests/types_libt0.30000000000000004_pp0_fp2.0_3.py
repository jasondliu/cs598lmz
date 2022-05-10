import types
types.MethodType(f, None, class_name)

# 这样，我们就给MyList增加了一个add方法
L = MyList()
L.add(1)
print(L)
# [1]

# 通常情况下，动态语言允许我们在程序运行时给类动态的添加方法，当然也可以动态的添加属性

# 实例属性和类属性
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性
# 给实
