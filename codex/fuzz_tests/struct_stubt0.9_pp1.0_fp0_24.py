from _struct import Struct
s = Struct.__new__(Struct)
s.size = 5

def pack(fmt, word):
    return s.pack(fmt, word)

def unpack(s):
    self = Struct()
    self.size = 5
    self.unpack = lambda f, w: s
    return self.unpack

unpack = unpack(pack('4sH', 'data', 0xC7BA))

def naive_binary_search(word, words):
    # implement me
    lo, hi = 0, len(words)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if unpack(word) < words[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


# exploit
def ret2csu(rdi, rsi, rdx, read_got_addr, read_plt, bss_addr, ret):
    """
    rdi = ; # fd
    rsi = ; # buf
    rdx = ; # size
    """
    assert rdx % 8 == 0

   
