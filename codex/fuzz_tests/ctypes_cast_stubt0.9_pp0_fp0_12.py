import ctypes
ctypes.cast(100, ctypes.py_object)
 
 ctypes.cast(100, ctypes.c_char_p)
 
ctypes.cast("H", ctypes.py_object)
 
 
[ord(x) for x in "H"]
 
ctypes.cast("H", ctypes.c_char_p)
 
t = "mystring"

ctypes.c_char_p.from_buffer("abc")
 
 
 

ctypes.cast("this is  a str", ctypes.c_void_p)
 
ctypes.addressof()
 
 
 
 
next(x for x in range(2**31) if (x | 0) > x)
 
 
 

n = -1
while True:
  if bin(n) == bin(n | 0):
    break
  n -= 1
    
    
    

n = 0
while True:
  if bin(n) == bin(n & (-n)):
    break
  n += 1
 
 
