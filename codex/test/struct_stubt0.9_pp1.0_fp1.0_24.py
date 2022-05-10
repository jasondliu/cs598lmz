from _struct import Struct
s = Struct.__new__(Struct)  # Direct construction not allowed
data = bytes('abcdefgh', 'utf-8')
print('data ', data, ' length ',len(data))
i = 5

# Call set_format to create a new
# struct format string dynamically 
s.set_format(data, i)

# Standard featurs work now
print(s.unpack(data))
