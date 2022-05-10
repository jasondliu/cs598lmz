fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
# fn()

# gi.__next__()
# f = gi.__next__
# f()
# gi.__next__ = None
# f()

# a = (i for i in ())
# a.__code__ = None
# # a.__next__()
# # a.__next__.__globals__
# a.__next__.__globals__ = (1, 2, 3)
# a.__next__()

# import sys
# import time

# def get_time(t):
#     time.sleep(t)
#     return time.time()

# def gen():
#     while True:
#         val = yield 1
#         print(val)

# def main():
#     g = gen()
#     g.send(None)
#     print(get_time(1))
#     print(get_time(1))
#     print(get_time(1))
#     print(get_time(1))
#     print(get_time(1))
