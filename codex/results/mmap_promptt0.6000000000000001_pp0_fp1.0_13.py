import mmap
# Test mmap.mmap(0, 1, tagname='Global\test')

# import mmap

# fd = os.open('test.dat', os.O_CREAT | os.O_TRUNC | os.O_RDWR)
# os.write(fd, b'\x00' * mmap.PAGESIZE)
# m = mmap.mmap(fd, mmap.PAGESIZE, tagname='test')
# m.close()
# os.close(fd)

# class Test(object):
#     def __init__(self):
#         self.a = 10
#         self.b = 20

# t = Test()

# class Test(object):
#     def __init__(self):
#         self.a = 10
#         self.b = 20

# t = Test()

# import ctypes
# def func(a, b):
#     return a + b

# libc = ctypes.CDLL(None)
# # print(ctypes.cast(func, ctypes.c_void_p).value)
