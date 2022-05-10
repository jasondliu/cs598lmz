import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()

'''

import sys

def read_input(filename):
    with open(filename, 'r') as f:
        return f.read()

def decode_input(input):
    return input.splitlines()

def main():
    filename = 'input.txt'
    input = read_input(filename)
    print(len(decode_input(input)))

if __name__ == '__main__':
    main()
