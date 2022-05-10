import threading
threading.stack_size(268435456)
sys.setrecursionlimit(10**9)

def main():
    stdin = open(0)
    data = stdin.read().split()
    n, k = int(data[0]), int(data[1])
    a = [int(i) for i in data[2:]]
    a.sort()
    print(a[-1] - a[0])

if __name__ == '__main__':
    main()
