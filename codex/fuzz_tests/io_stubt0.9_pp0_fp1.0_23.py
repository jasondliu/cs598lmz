import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# import threading
#
# event = threading.Event()
# def f():
#     event.set()
#     f()
#
# threading.Thread(target=f).start()
# event.wait()
#
# if 1:
#     import builtins
#     print(dir(builtins))
#     print(builtins.__all__)

# from . import datetime
#
# print(sys.modules['datetime'].__getattribute__)
# print(sys.modules['__builtin__'].__getattribute__)
# print(1)

# много-уровневый import
# from .a import b
# from .a.b import c
# from .a.b.c import d
#
# from .a import b
# from .a.b import c
# from .a.b.c import d
#
# class AAA:
#     pass
#
# class BBB(AAA):
#     class CCC:
#         class DDD:

