from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# call_function
#   LOAD_FAST 0 (x)
#   LOAD_FAST 1 (y)
#   CALL_FUNCTION 2
#   RETURN_VALUE

#   LOAD_GLOBAL              0 (foo)
#   LOAD_CONST               1 ('x')
#   LOAD_CONST               2 ('y')
#   CALL_FUNCTION            2
#   RETURN_VALUE

#   LOAD_GLOBAL              0 (foo)
#   LOAD_CONST               1 (1)
#   LOAD_CONST               2 (2)
#   CALL_FUNCTION            2
#   RETURN_VALUE

#   LOAD_GLOBAL              0 (foo)
#   LOAD_CONST               1 (1)
#   LOAD_CONST               2 (2)
#   CALL_FUNCTION            2
#   RETURN_VALUE

#   LOAD_GLOBAL              0 (foo)
#   LO
