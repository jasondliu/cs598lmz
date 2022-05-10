import mmap
import sys
import os

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: %s <filename> <word>" % sys.argv[0])

    f = open(sys.argv[1], "r+")
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    word = sys.argv[2]
    print("Replacing all instances of '%s' with '%s'." % (word, word.upper()))

    last_found = 0
    while True:
        next_offset = s.find(word, last_found + 1)
        if next_offset == -1:
            break
        s[next_offset:next_offset + len(word)] = word.upper()
        last_found = next_offset
    s.close()
    f.close()

if __name__ == '__main__':
    main()
