import sys, threading
threading.Thread(target=lambda: sys.stdout.write('threading')).start()
print sys._current_frames()[0].f_locals
print sys.getrecursionlimit()
print sys.getrefcount(sys)
print sys.getsizeof(sys)
print sys.getwindowsversion()
sys.exit(0)
print sys.getcheckinterval()
print sys.getallocatedblocks()
print sys.getfilesystemenco
