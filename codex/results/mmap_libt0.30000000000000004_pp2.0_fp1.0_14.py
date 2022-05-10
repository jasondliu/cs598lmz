import mmap
import sys
import re
import os

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 %s <input_file> <output_file>" % sys.argv[0])
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r") as f:
        with open(output_file, "w") as out:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                if line[0] == '#':
                    continue
                if line[0] == '>':
                    out.write(line + "\n")
                    continue
                out.write(line.upper() + "\n")

if __name__ == "__main__":
    main()
