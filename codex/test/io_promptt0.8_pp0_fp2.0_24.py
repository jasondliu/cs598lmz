import io
# Test io.RawIOBase
import sys
# Test io.StringIO, io.BytesIO


if __name__ == "__main__":
    print(sys.version)
    print()

    # io.FileIO

    print("io.FileIO")
    # create a temp file
    fp = open("tttemp.txt", "w+")
    print("fp:", fp)   # <_io.TextIOWrapper name='tttemp.txt' mode='w+' encoding='cp1252'>
    print(fp.fileno())   # 31    # the actual file descriptor
    print(fp.isatty())   # False
    print(fp.readable()) # True
    print(fp.seekable()) # True
    print(fp.writable()) # True
    print()
    fp.close()
    print()

    # only in Python 3.7+:
