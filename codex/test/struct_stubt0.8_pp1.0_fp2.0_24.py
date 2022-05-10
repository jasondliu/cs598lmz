from _struct import Struct
s = Struct.__new__(Struct).__init__('=f')
print(s)
#struct.Struct('=f')
#The above doesn't work for me.
