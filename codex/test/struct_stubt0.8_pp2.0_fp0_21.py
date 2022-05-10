from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

# Disable buffering to get a traceback on these objs
if sys.version_info[0] >= 3:
    sys.stdout = sys.stderr = Unbuffered(sys.stdout)

