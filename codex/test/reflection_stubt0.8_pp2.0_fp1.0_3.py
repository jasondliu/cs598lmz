fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_frame.f_code
fn.__code__

# 大多数函数都是由底层解释器实现的，因此其 __code__ 对象中实际上存储着指向 C 实现的一个函数指针。
