from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
f = s.unpack_from
print f(b'\x01\x00\x00\x00', 0)

# >>> f(b'\x01\x00\x00\x00', 0)
# (1,)
```

这样我们就可以将 `unpack_from` 函数用在任何 `Struct` 实例上了。

不过这样的写法有一点不妥，因为我们假设 `Struct` 类的实例只存在一个 `format` 属性，而事实上 `unpack_from` 可能需要更多的属性，所以我们可以使用 `functools.partial` 来
