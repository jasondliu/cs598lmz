import mmap
import struct
from pathlib import Path


def main():
    found = Path('found_match.txt')
    not_found = Path('not_found.txt')

    files = list(Path().glob("*"))
    fn = files.pop(0)


# abrir cada archivo cada vez
    f = open(fn, 'rb')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    for fn in files:
        print(fn)
        with open(fn, 'rb') as f1:

            s1 = mmap.mmap(f1.fileno(), 0, access=mmap.ACCESS_READ)

            pos = s.find(s1)

            if pos != -1:
                found.write_text(f"MATCHED {pos}  {fn}\n")
            else:
                not_found.write_text(f"NOT MATCHED {fn}\n")


main()
