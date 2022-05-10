import bz2
bz2.compress('a')

try:
    import lzma
except ImportError:
    pass
else:
    lzma.compress('a')

benchpep = """
    import io, random, sys
    import re, string, random

    def random_letters(size=6, chars=string.ascii_uppercase):
        return ''.join(random.choice(chars) for _ in range(size))

    def random_number(size=6):
        return ''.join(str(random.randint(0,9)) for _ in range(size))


    def setup():
        global data, fn
        data = b''.join(random_number() for i in range(4)) + b' ' + \
               b''.join(random_letters() for i in range(6)) + b' ' + \
               b''.join(random_number() for i in range(5)) + b' ' + \
               b''.join(random_letters() for i in range(7)) + b'\\n'
        fn = test.test_
