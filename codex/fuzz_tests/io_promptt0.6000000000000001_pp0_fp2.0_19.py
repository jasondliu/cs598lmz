import io
# Test io.RawIOBase.readinto()

def len_test(fname, size):
    f = open(fname, "rb")
    n = f.readinto(bytearray(size))
    print(f"readinto(bytearray({size})) -> {n}")

len_test("/dev/null", 1)
len_test("/dev/null", 2)
len_test("/dev/null", 3)
len_test("/dev/null", 4)
len_test("/dev/null", 5)
len_test("/dev/null", 6)
len_test("/dev/null", 7)
len_test("/dev/null", 8)
len_test("/dev/null", 9)
len_test("/dev/null", 10)
