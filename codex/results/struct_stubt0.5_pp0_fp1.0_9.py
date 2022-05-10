from _struct import Struct
s = Struct.__new__(Struct)

# Как объекты Struct представляют информацию о своем формате?
# Свойство экземпляра s.format возвращает строку со значением формата,
# а свойство s.size возвращает длину поля в байтах.
s.format = '<3s3sHH'
s.size = struct.calcsize(s.format)

# Как использовать объекты Struct?
# Выз
