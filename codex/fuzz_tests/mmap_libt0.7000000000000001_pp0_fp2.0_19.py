import mmap
import time
#
# file_obj = open("dictionary.txt","r+b")
# mm = mmap.mmap(file_obj.fileno(),0,access=mmap.ACCESS_READ)
#
# print mm.readline()
# print mm.tell()
# mm.seek(0)
# print mm.readline()
# mm.seek(0)
# print mm.readline()
# mm.close()


# def handler(signum,frame):
#     print 'Signal handler called with signal',signum
#
# def test():
#     while True:
#         print "sleeping"
#         time.sleep(5)
#
# signal.signal(signal.SIGTERM,handler)
#
# if __name__ == "__main__":
#     test()

import sys
import time
#
# def handler(signum, frame):
#     print "got signal", signum
#     if signum == signal.SIGTERM: # TODO: remove if not needed
#         print "
