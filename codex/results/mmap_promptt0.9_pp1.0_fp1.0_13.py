import mmap
# Test mmap.mmap(0,1, access=mmap.ACCESS_WRITE)
# print(mmap.mmap.__doc__)

# with open("lorem.txt", "r+") as f:
#     m = mmap.mmap(f.fileno(), 0)
#     # print(len(m))
#     # print(m[0:10])
#     print(ord(m[len(m)-1]))
#     # m.seek(1)
#     m.read_byte()
#     print(ord(m[len(m)-1]))
#     # m.seek(17)
#     # m.write(b"hello")
#     m.resize(len(m)+100)
#     m[len(m)-1] = '0'
#     print(m.read(10))
#     # m.close()
m = mmap.mmap(0, len(test_string), access=mmap.ACCESS_WRITE)
# when append the test_string to the end of the mmap string
m
