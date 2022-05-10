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
sys.stdin = File()

file = sys.stdin

order = [115, 111, 114, 116, 101, 100]

def swap(a, b):
    tmp = view[a]
    view[a] = view[b]
    view[b] = tmp

def sort(array, size, left=0):
    for i in range(left, left+size):
        for j in range(i+1, left+size):
            if array[i] > array[j]:
                swap(i, j)

def validate_win(array, size):
    for i in range(size):
        if array[i] != order[i]:
            return False
    return True

def validate_lose(array, size):
    for i in range(size):
        if array[i] == order[i]:
            return False
    return True

def encrypt_flag(flag):
    flag_str = str(flag)
    flag_str = flag_str + '\x00' * (32 - len(flag_str))
