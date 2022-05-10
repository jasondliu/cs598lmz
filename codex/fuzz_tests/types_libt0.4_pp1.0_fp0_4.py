import types
types.MethodType(lambda self: self.__class__.__name__, None, type)
# 'type'

# class C: pass
# C.__name__ = property(lambda self: 'foo')
# C().__name__
# 'foo'

# class C: pass
# C.__name__ = property(lambda self: 'foo')
# C.__name__
# <property object at 0x7f7e6d1d0c28>

# class C: pass
# C.__name__ = property(lambda self: 'foo')
# C.__name__ = 'bar'
# C.__name__
# 'bar'

# class C: pass
# C.__name__ = property(lambda self: 'foo')
# C.__name__ = 'bar'
# C().__name__
# 'foo'

# class C: pass
# C.__name__ = property(lambda self: 'foo')
# C.__name__ = 'bar'
# C.__name__ = 'baz'
# C().__name__
