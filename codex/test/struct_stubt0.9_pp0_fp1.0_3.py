from _struct import Struct
s = Struct.__new__(Struct); s._fields_ = [('name', 's'),('sh_name', 'H'),('type', 'I'),('flags', 'I'),('addr', 'Q'),('offset', 'Q'),('size', 'Q'),('link', 'I'),('info', 'I'),('align', 'Q'),('entsize', 'Q'),('elements', object)]
