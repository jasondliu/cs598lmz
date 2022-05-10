import mmap
import random
import time
import os
import sys

def main():
    file_size = int(sys.argv[1])
    file_name = "test.dat"
    print("file size:", file_size)
    with open(file_name, "wb") as f:
        f.truncate(file_size)

    while True:
        try:
            with open(file_name, "r+b") as f:
                mm = mmap.mmap(f.fileno(), 0)
                while True:
                    mm.seek(random.randint(0, file_size-1))
                    mm.write(bytes(str(random.randint(0, 9)), "ascii"))
                    # print(mm[0])
                    time.sleep(random.randint(0, 5))
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)

