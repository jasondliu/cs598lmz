from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 使用__new__方法创建的类和直接使用class语句创建的类没有本质上的区别，
# 但是使用__new__可以让我们在创建类的时候控制更多的细节。
# 例如，我们可以让一个类支持接受关键字参数，这在使用class语句创建类时是不可能的。

# 使用关键字参数
import operator
