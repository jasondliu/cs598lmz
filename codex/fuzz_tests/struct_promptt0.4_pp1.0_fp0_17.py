import _struct
# Test _struct.Struct

def check_sizeof(fmt):
    print(fmt, _struct.calcsize(fmt))

check_sizeof('b')
check_sizeof('h')
check_sizeof('i')
check_sizeof('l')
check_sizeof('q')
check_sizeof('B')
check_sizeof('H')
check_sizeof('I')
check_sizeof('L')
check_sizeof('Q')
check_sizeof('f')
check_sizeof('d')
check_sizeof('P')
check_sizeof('P#')
check_sizeof('s')
check_sizeof('s#')
check_sizeof('p')
check_sizeof('p#')
check_sizeof('c')
check_sizeof('?')
check_sizeof('=b')
check_sizeof('=h')
check_sizeof('=i')
check_sizeof('=l')
check_sizeof('=q')
check_sizeof('=B')
check_sizeof('=H')

