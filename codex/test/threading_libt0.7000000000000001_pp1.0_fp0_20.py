import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
f_inf = float('inf')
mod = 10**9+7

def main():
    S = input()   
    ans = f_inf
    for i in range(len(S)-2):
        ans = min(ans, abs(753 - int(S[i:i+3])))
    print(ans)


if __name__ == '__main__':
    main()
