from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
print(s.size)

#构造一个空的结构
print(s.pack(1, False, 3.14159))
#使用 _make 方法构建一个结构体实例
t = s.unpack(_)
#访问字段
t[0]

#使用 _asdict 方法把元组以命名元素的方式返回，可以被构造成collections.OrderedDict的实例
t = t._asdict()
print(t)
#使用**操作符把元组里的信息扩展到命名关键字参数中去
t
