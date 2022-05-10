from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab'.encode('utf-8'), 2.7)

# 2.2.2
# from _struct import Struct
# s = Struct.__new__(Struct)
# s.__init__('I 2s f')
# s.pack(1, b'ab', 2.7)

# 2.2.3
# from _struct import Struct
# s = Struct.__new__(Struct)
# s.__init__('I 2s f')
# s.pack(1, b'ab', 2.7)

# 2.2.4
# from _struct import Struct
# s = Struct.__new__(Struct)
# s.__init__('I 2s f')
# s.pack(1, b'ab', 2.7)

# 2.2.5
# from _struct import Struct
# s = Struct.__new__(Struct)
# s.__init__('I 2s f')
# s.pack(1, b'ab', 2.
