import threading
threading.stack_size(512*1024)
sys.setrecursionlimit(10**9)

def main():
    inp = open('input.txt', 'r')
    out = open('output.txt', 'w')
    n = int(inp.readline())
    lst = list(map(int, inp.readline().split()))
    lst.insert(0, 0)
    dp = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i):
            dp[i] = max(dp[i], dp[j]+lst[i]-lst[j+1])
    out.write(str(dp[-1]))

threading.Thread(target=main).start()
