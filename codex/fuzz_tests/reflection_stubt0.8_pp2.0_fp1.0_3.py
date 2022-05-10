fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_frame.f_code
fn.__code__

# 大多数函数都是由底层解释器实现的，因此其 __code__ 对象中实际上存储着指向 C 实现的一个函数指针。
open.__code__

# 一些函数由 Python 代码实现，它们的 __code__ 属性的 co_filename 字符串包含定义该函数的源文件名，co_firstlineno 包含定义该函数的第一行所在的行号。
d = {}
exec("def foo(): pass", d, d)
foo = d["
