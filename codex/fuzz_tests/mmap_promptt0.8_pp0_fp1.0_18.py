import mmap
# Test mmap.mmap() with a file name.
def main():
    fd = os.open("mapfile.txt", os.O_CREAT | os.O_RDWR)
    os.write(fd, "Hello, Python!\n")
    m = mmap.mmap(fd, 0)
    print m.readline()
    os.lseek(fd, 0, 0)
    print m
    m.seek(5)
    print m.read(2)
    # mapfile_txt = file("mapfile.txt")
    # print "mapfile_txt.readline(): %s" % mapfile_txt.readline()
    # print "type(mapfile_txt): %s" % type(mapfile_txt)
    # print "id(mapfile_txt): %s" % id(mapfile_txt)

if __name__ == "__main__":
    main()
