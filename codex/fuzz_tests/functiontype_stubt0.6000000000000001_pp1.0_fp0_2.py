from types import FunctionType
a = (x for x in [1])
print(type(a))
print(FunctionType)

# 为什么list里面的元素不能是函数？
# 函数是不可哈希的， 不能作为key
# 用元组来替代list
# 元组可以放不同类型的元素

# 函数对象有个__name__属性，可以拿到函数的名字
# 闭包， 函数内部嵌套函数
# 闭包的特点是， 返回的函数还依赖于外部函数的变量， 实现
