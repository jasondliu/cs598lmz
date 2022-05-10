import mmap
# Test mmap.mmap()
#
#
#
#
#

def main():
    f = open("testfile", "w+")
    f.write("Hello World")
    f.close()

    f = open("testfile", "r+")
    m = mmap.mmap(f.fileno(), 0)
    m.write("Hello Python")
    m.seek(0)
