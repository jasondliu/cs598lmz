from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>h')
s.pack(1)

# 这里使用了_struct.Struct的__new__方法，
# 然后直接调用了Struct类的__init__方法，
# 这样就避免了调用__init__方法时，
# 会自动调用__new__方法创建一个实例的问题。
# 如果不这样做，那么就会报错：
# TypeError: object.__new__(Struct) is not safe,
# use Struct.__new__()

# 另外，__new__方法的第一个参数是cls，
# 表示
