from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 如果你使用的是 Python 2.6 或者更早的版本，你可能会喜欢使用 namedtuple() 函数来构建一个带字段名的元组和一个有默认值的命名元组类。
# 下面是一个例子：
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
sub
sub.addr
sub.joined
len(sub)
addr, joined = sub
addr
joined

# 命名元组的一个主要用途是将你
