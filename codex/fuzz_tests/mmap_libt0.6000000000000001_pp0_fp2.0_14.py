import mmap

def main():
    """
    main program
    """

    # open the file for reading
    f = open("lorem_ipsum.txt", "r")

    # open the file for writing
    fw = open("lorem_ipsum_mmap.txt", "w")

    # try to mmap the file
    try:
        mm = mmap.mmap(f.fileno(), 0)
    except ValueError:
        print("mmap failed")
        sys.exit(1)

    # write mmap to the file
    fw.write(mm.read())

    # close the files
    f.close()
    fw.close()

if __name__ == "__main__":
    main()
