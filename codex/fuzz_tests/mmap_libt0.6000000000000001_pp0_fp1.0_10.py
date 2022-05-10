import mmap
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: {} <filename> <byte to replace>".format(sys.argv[0]))
        return

    filename = sys.argv[1]
    byte_to_replace = int(sys.argv[2], 16)
    print("Replacing {} in {}".format(byte_to_replace, filename))

    with open(filename, 'r+b') as f:
        binary_data = mmap.mmap(f.fileno(), 0)

        for i in range(len(binary_data)):
            if binary_data[i] == byte_to_replace:
                print("Replacing at {}".format(i))
                binary_data[i] = 0x00

if __name__ == '__main__':
    main()
