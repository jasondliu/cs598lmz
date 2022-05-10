from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x01')

# 如果你想通过某个类创建实例，但是又不想调用 init() 方法，你可以使用 new() 方法，
# 它只是返回一个未初始化的实例。

# 如果你仅仅只是想获取某个类的对象而不去调用 init() 方法，
# 那么你可以使用 type() 来做到这一点。

import os
import io

# io.BytesIO()
# io.StringIO()
