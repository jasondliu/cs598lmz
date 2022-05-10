import bz2
# Test BZ2Decompressor
dec = bz2.BZ2Decompressor()
data = deque(dec.decompress(data, max_length=50))
def decompress(data):
    data = deque(data)
    try:
        while True:
            if len(data) <= 0:
                raise EOFError
            token = data.popleft()
            if token == b'(':
                n = b''
                while data[0] != b'e':
                    n += data.popleft()
                n = int(n)
                c = data.popleft()
                if c != b'e':
                    raise RuntimeError

                data = deque(b''.join([data[i:i + n] for i in range(0, len(data), n)])) + data
            elif token.isdigit():
                n = b''
                while data[0] != b':':
                    n += data.popleft()
                n = int(n)
                if data.popleft() != b':':
                    raise RuntimeError

                s =
