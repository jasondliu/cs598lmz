import threading
threading.stack_size(67108864)

mod = 1000000007

def fibMemo(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibMemo(n-1, computed) + fibMemo(n-2, computed)
    return computed[n]
    
def calc(n):

    if n == 0:
        return 0

    p = 1
    for i in range(1, n):
        p = (p * i)%mod

    return (fibMemo(2*n-2) - fibMemo(n) + p)%mod

t = int(input())
for i in r
