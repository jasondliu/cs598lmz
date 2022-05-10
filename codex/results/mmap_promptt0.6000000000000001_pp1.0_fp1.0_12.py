import mmap
# Test mmap.mmap
#m = mmap.mmap(0, 4096, "MAP_SHARED", mmap.ACCESS_WRITE)
#m.write("hello world")
#m.close()

import multiprocessing
# Test multiprocessing.Value
#from ctypes import c_int
#val = multiprocessing.Value(c_int, 0)
#val.value = 3

# Test multiprocessing.Array
#from ctypes import c_int
#arr = multiprocessing.Array(c_int, range(10))
#print arr[3]

# Test multiprocessing.Manager
#from multiprocessing import Pool
#from multiprocessing.managers import BaseManager
#
#class MyManager(BaseManager):
#    pass
#
#MyManager.register('list', list)
#
#m = MyManager()
#m.start()
#
#l = m.list()
#l.append(1)
#print l
#
#pool = Pool(processes=4)
#def f(l
