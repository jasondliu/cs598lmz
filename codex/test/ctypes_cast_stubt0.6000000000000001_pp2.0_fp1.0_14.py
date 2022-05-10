import ctypes
ctypes.cast('abc', ctypes.c_char_p).value

#其他

#1.字符串和数组的转换
#字符串转数组
import array
s = 'This is the array.'
