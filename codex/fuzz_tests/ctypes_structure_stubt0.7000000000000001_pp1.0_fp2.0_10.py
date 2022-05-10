import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint.in_dll(ctypes.CDLL(None), 'x')
    y = ctypes.c_uint.in_dll(ctypes.CDLL(None), 'y')
    z = ctypes.c_uint.in_dll(ctypes.CDLL(None), 'z')

def main():
    s = S()
    print(s.x, s.y, s.z)

if __name__ == '__main__':
    main()
</code>
Output:
<code>$ python3 test.py 
0 0 0
</code>

