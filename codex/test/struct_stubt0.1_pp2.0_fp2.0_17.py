from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 可以使用类来创建实例，但是通常不这么做。
# 如果你真的需要这样做，你应该使用类的构造器，通过调用类的 __new__ 方法来创建实例，然后调用 __init__ 方法对实例进行初始化。

# 如果你想创建一个可以被继承的类，你应该显式的继承 object 类。
# 如果你不
