import sys, threading

def run():
    with open('in.txt') as f:
        lines = f.readlines()
    n = int(lines[0])
    print(n)
    for i in range(1, n+1):
        print(i)
        sys.stdout.flush()
        ans = int(lines[i])
        guess = int(input())
        if ans != guess:
            print('Wrong Answer')
            exit(0)
    print('Accepted')

def main():
    sys.setrecursionlimit(10**9)
    threading.stack_size(2**27)
    thread = threading.Thread(target=run)
    thread.start()

main()
