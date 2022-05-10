from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'iiii'
L.append(list(s.unpack_from(i)))
print(L)

# import hashlib
#
# x = hashlib.sha1()
# x.update(b"hello world")
# print(x.hexdigest())


# print(aa[:64])
# a = "ABCDEFGHIJKLMNOPQ"
# print(a[::-1])

# b = a[:8] + ' '+ a[8:]
# print(b)

# d = {'a': [1, 2], 'b':[3, 4]}
# n = lambda x: x[0]
# c = list(e for e in d.keys() if n(e) >= '3')
# print(c)
# import tensorflow as tf
# a = tf.get_variable('a')
# print(a)


# import jpype
# import os

# os.environ['CLASSPATH'] = jpype.getDefaultJVMPath()
# jvm
