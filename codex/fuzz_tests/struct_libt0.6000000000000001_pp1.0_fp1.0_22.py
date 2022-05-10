import _struct
from array import array

def main():
    buf = array('i', [0] * 10)
    f = open('data.bin', 'wb')
    s = _struct.Struct('i' * 10)
    s.pack_into(buf, 0, *range(10))
    f.write(buf.tostring())
    
if __name__ == '__main__':
    main()
