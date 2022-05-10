import ctypes
ctypes.cast(0, ctypes.py_object).value

# 定义结构体  
class st_account_info(ctypes.Structure):  
    _fields_ = [("name", ctypes.c_char * 256),  
                ("day", ctypes.c_char * 256)]  

# 定义返回数据类型  
Lib_GetAccount = ctypes.CDLL('../lib/libAT_python_c.so').getAccount
Lib_GetAccount.restype = ctypes.POINTER(st_account_info)

# 调用函数  
pst_account_info = Lib_GetAccount()  
account_info = pst_account_info.contents  
print account_info.name, account_info.day  

# 如果结构体内还有结构体，则还是如上方式，利
