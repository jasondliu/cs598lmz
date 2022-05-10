from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.pack(1)

# 而使用__new__方法可以避免这个问题，先创建一个空对象，然后通过__init__方法去初始化它
s = Struct.__new__(Struct)
s.__init__('>H')
s.pack(1)

# 在Python中，实例化某个类的时候，会调用__new__方法，然后，返回的实例对象会调用__init__方法，这样就完成了一个实例的创建过程
# 其实，
