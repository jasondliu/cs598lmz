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

