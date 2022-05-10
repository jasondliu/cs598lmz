from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# 从源码中看到，Struct的__new__方法是空的，所以不能直接调用__new__方法，
# 而是要调用Struct的类方法，这个类方法会调用__new__方法，并且传入format参数
# 所以，Struct的实例化只能使用类方法来实现，即s = Struct('i')

# 总结：
# 1. 实例化时，自动调用__new__方法
# 2. __new__方法的第一个参
