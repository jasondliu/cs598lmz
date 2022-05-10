from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.pack(1)

# 这里的Struct是_struct模块中的一个类，这个类的__new__方法接受一个格式字符串作为参数，然后创建并返回一个结构化解析类型的对象
# 这个对象的pack方法可以将任意数据打包成字节字符串

# 对于大多数的Python类来说，__new__方法的作用是返回一个初始化的实例，而__init__方法的作用是
