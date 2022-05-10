import ctypes
# Test ctypes.CField
class FixedArray:
    type_type=ctypes.c_int*3
    def __init__(self):
        self._temp=[]
    def add(self, x):
        assert not(x in self._temp)
        assert 1<= x <= 3
        self._temp.append(ctypes.c_int(x))
    def get(self):
        return self.type_type(*self._temp)

array=FixedArray()
array.add(1)
array.add(2)
array.add(3)
print(array.get())


"""
In C’s *array.h  header file...

#define _FIBIX(type,n)	type[n]
#define _FIB(type,n)	  _FIBIX(type,n)

#define _FARRAY(type,n)	  _FIB(type,n)

#define _FARRAYDEF(type,name)	  type name[]; 

#define _FARRAYMSG(type,n,id)	 
