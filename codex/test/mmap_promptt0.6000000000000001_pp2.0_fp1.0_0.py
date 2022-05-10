import mmap
# Test mmap.mmap for read and write.

def main():
    f = open('mmap.txt', 'w+')
    f.write('Hello, world!')
    f.close()
    f = open('mmap.txt', 'r+')
    m = mmap.mmap(f.fileno(), 0)
