import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_char_p)
LIB = ctypes.cdll.LoadLibrary(r"c:\lena\PyScripts\cpp\cppSampleFunc.dll")
print 'loaded cpp dll'


@FUNTYPE
def cppFunc(pStruct, intensity, size, output):
  print 'python func called'
  print intensity.value
  print size.value
  if (size.value & 1) == 0:
    size.value += 1
  print pStruct
  print pStruct[0]
  print pStruct[1]
  print pStruct[2]
  print pStruct[3]

  print output


def main():
  pStruct = ctypes.c_int * 4
  dat = pStruct(1, 2, 3, 4)
  print dat
  LIB.cppFunc(dat, ctypes.c_int(10), ctypes.c_int(20), 'My output')
  LIB.setpyFuncPo
