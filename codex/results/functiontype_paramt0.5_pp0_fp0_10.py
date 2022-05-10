from types import FunctionType
list(FunctionType(lambda: None, {}).__globals__)

# [{}]

# 在Python3.3中，函数的__globals__属性返回的是它所在的模块的命名空间，这样可以避免上面的这种情况，但是它不能够正确处理闭包。
#
# 因为在Python3.3中，闭包的__globals__属性返回的是自由变量所在的命名空间，这样就可以获得自由变量的值，而不需要使用cell对象。
#
# 但
