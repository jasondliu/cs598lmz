from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i")
s.pack(1)

# 为了让这个类变得更加通用，可以将Struct类的定义放在一个名为struct的模块里，
# 然后使用import的时候通过from语句导入特定的类。

# 在下面的代码中，我们使用from语句导入了Struct类，并且给它取了一个别名——_Struct。
from struct import Struct as _Struct

_struct = _Struct.__new__(_Struct)
_struct.__init__("i")
_struct.pack(1)

# 在这个例子中，
