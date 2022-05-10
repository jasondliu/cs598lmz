import threading
threading.stack_size(2**26)
sys.setrecursionlimit(10**7)

def main():
    stdin = open(0)
    A, B, C, D = map(int, stdin.readline().split())
    print(min(B, D) - max(A, C))

threading.Thread(target=main).start()
