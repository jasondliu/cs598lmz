from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 注意到这里我们让s变量引用一个已经存在的Struct对象。
# 当我们调用s.__init__('>I')时，它会改变s所引用的对象，
# 而不是创建一个新的Struct对象并将s重新绑定到它。
#
# 对于一个类来说，__new__方法是静态方法（也就是说，它不需要创建对象实例就可以运行），
# 而__init
