import mmap
# Test mmap.mmap
with open("test.txt", "w+") as fd:
    text = mmap.mmap(fd.fileno(), 0, prot=mmap.PROT_READ|mmap.PROT_WRITE, flags=mmap.MAP_SHARED)
    with text:
        print("Read in line by line using file.readline")
        print(text.readline().decode())
        print(text.readline().decode())
        print(text.readline().decode())
        print(text.readline().decode())
        print(text.readline().decode())
        text.seek(0)
        print("Read in a block with file.read")
        print(text.read().decode())
        text.seek(0)
        print("Simple slice")
        print(text[6:12].decode())
        print("Iterate over lines")
        for line in text:
            print(line.decode())
        print("Iterate over lines with for")
        for line in range(0, text.size(), 10):

