from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 在给定的fmt字符串上调用Struct.__new__()
# 实例化一个新的Struct对象
# 然后调用其__init__()方法
# 初始化它
# 并返回它
# 可以看到，Struct的实例支持的方法和属性
# 都是由类型对象定义的
# 它们只是被实例化的对象所引用罢了
# 实例对象只是一个普通的命名空间
# 可以用
