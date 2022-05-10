import threading
threading.stack_size(4096000000)

import sys

def main():
    while True:
        s, out = sys.stdin.readline(), ''
        if not s: break
        n = len(s)
        for i in range(n):
            for j in range(n-1, i-1, -1):
                if s[i] != s[j]: continue
                for k in range(i,j):
                    if s[k] != s[k+1]: break
                if k >= j: continue
                tmp = s[j:i-1:-1]
                if out == '' or len(tmp) >= len(out):
                    out = tmp
        if out == '': print('No solution!')
        else: print(out)

thread = threading.Thread(target = main)
thread.start()
