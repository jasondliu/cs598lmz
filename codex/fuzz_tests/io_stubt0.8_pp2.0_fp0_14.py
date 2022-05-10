import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f # workaround for https://bugs.python.org/issue30252

#
# try:
#     f = io.FileIO("testfile", "w")
# except io.UnsupportedOperation as err:
#     print("UnsupportedOperation: {0}".format(err))
# except OSError as err:
#     print("OSError: {0}".format(err))
# else:
#     try:
#         f = open("testfile", "w")
#     except IOError as err:
#         print("IOError: {0}".format(err))
#     else:
#         try:
#             f.write("hello world\n")
#         finally:
#             f.close()
#    f = io.BufferedReader(io.FileIO("testfile", "r"))
#    try:
#        print(f.read())
#    finally:
#        f.close()
# finally:
#     try:
#         os.remove("testfile")
#     except:
#         pass
