import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

def fn1():
    try:
        f.read(1)
    except ValueError:
        print('ValueError')

def fn2():
    try:
        f.readinto(bytearray(10))
    except ValueError:
        print('ValueError')

def fn3():
    try:
        f.readinto1(bytearray(10))
    except ValueError:
        print('ValueError')

def fn4():
    try:
        next(f)
    except ValueError:
        print('ValueError')

def fn5():
    try:
        iter(f)
    except ValueError:
        print('ValueError')

def fn6():
    try:
        print(f)
    except ValueError:
        print('ValueError')

def fn7():
    try:
        print(f)
    except ValueError:
        print('ValueError')

def fn8():
    try:
        print(f.__next__())
    except ValueError:
        print('ValueError')
