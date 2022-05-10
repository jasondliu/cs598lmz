import ctypes
# Test ctypes.CFUNCTYPE
def function(x):
	return x**2

print 'function(8)=', function(8)
print 'chr(97)=', chr(97)

FT_func = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float)
FT_func.restype = ctypes.c_int

func = FT_func(function)
print 'func(3.)=', func(3.)
print 'func(4.)=', func(4.)
print 'func(5.)=', func(5.)

lib = ctypes.cdll.LoadLibrary('/home/t/Dropbox/myPrograms/C/liblibrary.so')
# lib = ctypes.cdll.LoadLibrary('/home/t/Dropbox/myPrograms/C/liblibrary.dylib')
# lib = ctypes.cdll.LoadLibrary('/home/t/Dropbox/myPrograms/C/library.dll')

print lib.count_vowel("AsIa")
print lib.count_vowel("Bbc")

