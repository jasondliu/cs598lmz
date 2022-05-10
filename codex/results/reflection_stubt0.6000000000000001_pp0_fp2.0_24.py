fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    fn()
except TypeError as e:
    print(e)

# TypeError: <lambda>() takes 0 positional arguments but 1 was given
# 但是如果给定参数的话，会发生什么呢？

fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn(1)

# 什么都没有。

# 所以，如果你认为这个陷阱会让你的程序产生运行时错误，那你就错了。它只是让你的程序做了一些额外的事情而已。

# 小结

#
