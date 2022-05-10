from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

# 不要使用继承，尤其是不要在没有必要的情况下继承 list 和 dict 这样的内置类型。
# 如果需要实现类似的行为，可以考虑使用集合模块中的 UserList 和 UserDict 类。

# 如果你打算编写大量用于数据编码的类，可以考虑使用描述器或者元类来实现。

#
