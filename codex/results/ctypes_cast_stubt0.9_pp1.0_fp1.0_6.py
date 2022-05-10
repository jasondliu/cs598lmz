import ctypes
ctypes.cast(a, py.Pointer(b)) # b指针类型
ctypes.cast(a, py.py_object) # 任意类型

'''
c_char:int8_t 
c_byte:uint8_t 
c_ubyte:uint8_t 
c_short:int16_t 
c_ushort:uint16_t 
c_int:int32_t 
c_uint:uint32_t 
c_long:long 
c_ulong:unsigned long 
c_longlong:int64_t 
c_ulonglong:uint64_t
c_float:float 
c_double:double 
c_void_p:void * 
py_object:PyObject
'''
'''
对ctype做一个简单的菜单
def sep_line():
    print('')
    print('-------------------------------------')
    print('')

sep_line()
