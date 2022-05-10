import bz2
# Test BZ2Decompressor from a generator

def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

@coroutine
def cat(next_coroutine):
    while True:
        next_coroutine.send(b"Hello\n")
        next_coroutine.send(b"World\n")

@coroutine
def bz2decompress(next_coroutine):
    while True:
        next_coroutine.send(bz2.decompress(yield))

@coroutine
def write(filename):
    with open(filename, "wb") as f:
        while True:
            f.write(yield)

cat(bz2decompress(write("hello.txt")))

with open("hello.txt", "rb") as f:
    print(f.read())

# Works but not what we want. We want a stream and for bz2decompress() to decompress
# whatever it gets from cat() and send
