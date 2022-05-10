import threading
threading.stack_size(67108864)

def find_cube(n):
    if (n < 12):
        return -1
    else:
        return n * n * n

def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        print find_cube(n)

if __name__ == '__main__':
    thread = threading.Thread(target = main)
    thread.start()
