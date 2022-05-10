import mmap

filepath = "ascii.txt"

with open('ascii.txt', 'w+') as f:
    f.write("hello world!")

with open("ascii.txt") as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print("read 1:", m.read(5))
        print("read 2:", m[:5])
