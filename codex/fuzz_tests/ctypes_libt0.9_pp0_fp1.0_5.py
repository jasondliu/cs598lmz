import ctypes
ctypes.string_at(ctypes.byref(p1),ctypes.sizeof(p1))

, 这样就可以解释问题了


p1=ctypes.POINTER(ctypes.c_int)
p1=ctypes.cast(P1_ptr,p1)
ctypes.pointer(p1).contents
#用ctypes.byref(p1)也可以直接指向p1
,这样也可以得到数值

以上，主要是为了弄清楚:byref()和POINTER()在普通类型和指针类型的一些用法的一些区别


ctypes.byref(p1)<-- POINTER 指针的类型的
