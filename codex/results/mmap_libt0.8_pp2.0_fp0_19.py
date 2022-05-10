import mmap

def create_file(filename, data):
    file = open(filename, "w+b")
    file.write(data)
    file.close()

def read_file(filename):
    file = open(filename, "r+b")
    mm = mmap.mmap(file.fileno(), 0)
    while True:
        print mm.readline()

def main():
    buf = "a" * 4096 + "\n"
    buf += "b" * 4096 + "\n"
    buf += "c" * 4096 + "\n"
    buf += "d" * 4096 + "\n"
    create_file("./tmp.txt", buf)
    read_file("./tmp.txt")


if __name__ == "__main__":
    main()
