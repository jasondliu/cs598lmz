from types import FunctionType
list(FunctionType(lambda x:x).__code__.co_code)  # [100, 0, 0, 100, 0, 0, 0, 1, 0, 0, 0, 0, 100, 0, 0, 83]
FunctionType(lambda:0).__code__.co_code  # b'\x64\x00\x00S'
FunctionType(lambda x:x).__code__.co_code  # b'`\x00\x00d\x00\x00\x00\x01\x00\x00\x00\x00`\x00\x00S'
FunctionType(lambda:lambda:0)().__code__.co_code  # b'd\x00\x00S'
FunctionType(lambda x:len(x))((1,2)).__code__.co_code  # b'c\x00\x00l\x01\x00\x00\x00\x01\x00\x00S'

# b'\x64\x00\x00S'
# 第一个字
