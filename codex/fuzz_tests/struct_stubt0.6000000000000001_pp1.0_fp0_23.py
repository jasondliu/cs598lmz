from _struct import Struct
s = Struct.__new__(Struct) # 注意这里
s.__init__('>i') # 传入endianess和int的format spec
s.size # 返回4

'''
这里我们使用__new__()创建了一个Struct类的实例，然后再调用__init__()方法来初始化它。这里
就是类的实例化过程，但是我们显式的调用了__new__()方法，这样就可以控制类的实例化。

通常情况下，我们使用类名直接调用__new__()方法来创建
