import threading
threading.stack_size(67108864)
sys.setrecursionlimit(2 ** 20)

def Input():
    return sys.stdin.readline()

#main
def main():
    N, M = map(int, Input().split())
    A = [int(x) for x in Input().split()]
    A.sort()
    for i in range(M):
        l, r = map(int, Input().split())
        print(sum(A[l-1:r]))

thread = threading.Thread(target=main)
thread.start()
