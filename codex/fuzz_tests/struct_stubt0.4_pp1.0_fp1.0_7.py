from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

# 这个例子中，我们使用了__new__()方法来创建类的实例，因为__init__()方法需要参数format，而__new__()不需要，
# 因此使用__new__()来创建实例。

# 在这个例子中，我们还看到了把一个字符串转换成字节对象的方法。
# 当使用encode()方法时，可以指定字符编码
