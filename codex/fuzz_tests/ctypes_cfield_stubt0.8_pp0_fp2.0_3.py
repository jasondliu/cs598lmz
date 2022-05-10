import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    p = ctypes.POINTER(S)()

    # ctypes.c_int.from_address should fail as its not a ctypes.Pointer
    try:
        p.contents.x.from_address(p)
    except TypeError as e:
        print(str(e))

# no crash with both python 2 and 3
main()

# Example output:
# 
# expected ctypes.POINTER instance instead of type 'CField'
