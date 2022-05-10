fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
# 程序在继续运行之前会抛出TypeError异常，并且回溯已经设置好了，提示信息是：
#  TypeError: __code__: generator can't be used in 'exec' mode
exec(fn.__code__)
# 所以我们只需要修改类型检查，让其忽略类型检查就可以击穿Py_single_input
print(fn.__code__.co_flags)
print(fn.__code__.co_flags & COF_MASK_OFLAGS)
fn.__code__.co_flags &= ~COF_MASK_OFLAGS
print(fn.__code__.co_
