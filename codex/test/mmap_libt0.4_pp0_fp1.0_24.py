import mmap
import re
import sys
import time

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        return

    with open(sys.argv[1], "rb") as f:
        mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
        data = mm.read()

    start = time.time()
    for _ in range(1000):
        re.findall(br"\d+", data)
    end = time.time()
    print("mmap: %s" % (end - start))

    start = time.time()
    for _ in range(1000):
        re.findall(br"\d+", data.decode("utf-8"))
    end = time.time()
    print("decode: %s" % (end - start))

if __name__ == "__main__":
    main()
