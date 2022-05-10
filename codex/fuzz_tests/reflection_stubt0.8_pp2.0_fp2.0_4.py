fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# class C(object):
#     def __init__(self):
#         self.x = 42
#     def __call__(self):
#         return 42
# c = C()
# # c.x = 24
# def f(a):
#     print('f:', a)
#     return a
# d = hstats(f)(10)
# d = hstats(c.__call__)(12)
# d = hstats(fn)()
