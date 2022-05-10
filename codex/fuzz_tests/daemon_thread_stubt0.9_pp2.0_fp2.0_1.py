import sys, threading

def run():
    while True:
        a, b = map(int, input().split(' '))
        c = a + b
        print(c)


def main():
    sys.stdin = open('in.txt')
    sys.stdout = open('out.txt', 'w')

    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()

    for _ in range(100000):
        print(1, 1)
        print(0, 0)

if __name__ == "__main__":
    main()
