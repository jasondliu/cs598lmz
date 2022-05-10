from types import FunctionType
list(FunctionType(lambda x:x,globals(),'f')(i) for i in range(10))

# 列表推导式的嵌套
# 列表推导式可以嵌套，但是嵌套的层数不宜过多，否则会使得代码难以阅读
# 嵌套的列表推导式的层数不宜过多，否则会使得代码难以阅读
# 列表推导式的嵌套
# 列表推导式可以嵌套，但是嵌套的层数不宜过多，否则会使得代码难
