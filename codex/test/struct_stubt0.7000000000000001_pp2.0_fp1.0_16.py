from _struct import Struct
s = Struct.__new__(Struct)
print(s)

# 可以发现，Struct对象在创建时，实际上是绑定了一个字符串，该字符串就是描述结构的编码。比如，我们可以用这个编码来初始化别的Struct对象。
s = Struct('>I') # 字节序大端 >
print(s.size)

# 我们发现，Struct对象除了支持format，还支持一个只有一个参数的方法，该方法的参数就是字节
