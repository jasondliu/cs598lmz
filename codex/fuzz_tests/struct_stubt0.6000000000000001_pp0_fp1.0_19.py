from _struct import Struct
s = Struct.__new__(Struct)
#s.format = 'hhl'
#s.format = 'hhi'
#s.format = 'bb'
s.format = 'b'
s.size = s.format.__sizeof__()

def get_records(filename, recordsize=s.size):
    with open(filename, 'rb') as f:
        chunks = iter(partial(f.read, recordsize), b'')
        return (s.unpack(chunk) for chunk in chunks)

def main(filename):
    for record in get_records(filename):
        print(record)

if __name__ == '__main__':
    main(sys.argv[1])
</code>
I want to read binary file and print out the values. It works fine for <code>s.format = 'hhl'</code> (short,short,long), but it doesn't work for <code>s.format = 'hhi'</code> (short,short,int). 
Input file:
<code>0000000: 0100 0000 0000 0000 0000 0000 0000 0000  ................
