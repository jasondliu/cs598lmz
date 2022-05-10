import mmap
# Test mmap.mmap
import contextlib


@contextlib.contextmanager
def open_mmap_file(filename, mode="r", length=10, access=mmap.ACCESS_WRITE):
    """This function opens the file by using mmap and
    allows to write to the file perfectly"""
    fileobj = open(filename, mode)
    fileobj.seek(0)
    map_obj = mmap.mmap(fileobj.fileno(), length, access=access)
    try:
        yield map_obj
    finally:
        map_obj.close()


def main():
    """This is the main function."""
    with open_mmap_file("mmap_test.txt", mode="w+", length=3000) as map_obj:
        map_obj[:24] = b"Why I love a mmap file."
        print("{}".format(map_obj[:]))


if __name__ == "__main__":
    main()
