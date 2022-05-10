import ctypes
ctypes.cast(p, ctypes.py_object).value

---

10 times faster than Python List, but consume much larger space

CPython stores a reference to each object in list
a long list of integers, 32 bytes, instead of 4 bytes
sparse list of large objects, up to 8x the size
  acceptable for large corpus or word2vec

c_list[i] = c_list[i] + (p,) for repeated adding, O(N)

c_list[i] = c_list[:i] + (new,) + c_list[i:] a new space will be allocated, O(N) will be slower

do not use:
  c_list += (...)
  c_list1 = c_list1 + c_list2
pay attention to the extra time and space wasted by copying



==

---

https://github.com/sdpython/pythran/blob/master/examples/size.py

b=np.zeros((1024,1024,1024))
print b.nbytes
print sys.getsizeof(b)

---

