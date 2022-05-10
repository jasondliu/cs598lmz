from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 如果你想要通过某个类创建实例并且还希望在实例创建过程中修改类，那么你可以使用定义一个特殊的 __prepare__() 方法。
# 比如，下面这个例子创建了一个元类，它在类定义的时候会插入一个方法：
import logging
from io import StringIO

def add_logging_level(level, level_name, method_name=None):
    if not method_name:
        method_name = level_name.lower()

   
