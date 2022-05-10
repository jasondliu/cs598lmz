import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return None
ctypes.pythonapi.PyCode_New(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# CHECK-LABEL: @"\01L_OBJC_METH_VAR_NAME_"
# CHECK-DAG:   [[FTY:%.*]] = type <{ [[INT]], i8* (i8*, i8*, ...)* }>
# CHECK-DAG:   call void ({{.*}}*, [[FTY]], [[INT]] {{.*}})
# CHECK:       ret

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
def my_fun(a, b, c):
  return a + b + c

# CHECK-LABEL: @"\01L_OBJC_METH_VAR_NAME_"
# CHECK-DAG:   [[FTY:%.*]] = type <{ [[INT]], i8* (i8*, i8
