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

