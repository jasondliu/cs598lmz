import ctypes
ctypes.cast('abc', ctypes.c_char_p).value

#其他

#1.字符串和数组的转换
#字符串转数组
import array
s = 'This is the array.'
a = array.array('c', s)#c代表字符型
a

#数组转字符串
a.tostring()

#2.字符串格式化
#%运算符
#%c	字符及其ASCII码
#%s	字符串
#%d	有符号整数(十进制)
#%u	无符号整数(十进制)
#%o	无符号整数(八进
