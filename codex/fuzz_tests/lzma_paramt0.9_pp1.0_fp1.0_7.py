from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self, what: b''

sys.stdin = io.BufferedReader(open(0, 'rb'))
sys.stdout = io.BufferedWriter(open(1, 'wb'))

c = LZMADecompressor()

with sys.stdin, sys.stdout:
    for buf in iter(lambda: sys.stdin.read(1024), b''):
        sys.stdout.write(c.decompress(buf))
        sys.stdout.flush()
