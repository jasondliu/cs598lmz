import ctypes
ctypes.cast(addr, ctypes.py_object).value

# 总结：
# 因为Python的字符串是不可变的，因此，字符串类型是不可变的，
# 而list是可变的，所以，list是可变的。
# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c', 'b', 'a']
a.sort()
print(a)
a = 'abc'
a.replace('a', 'A')
print(a)

# 使用key-value存储结构的dict在Python中非常有
