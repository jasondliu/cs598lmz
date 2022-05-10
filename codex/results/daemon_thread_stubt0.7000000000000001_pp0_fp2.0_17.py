import sys, threading

def run():
    sys.stdin = open('./in.txt', 'r')
    sys.stdout = open('./out.txt', 'w')
    n = int(input())
    for i in range(n):
        s = input()
        if len(s) < 4:
            print("Case #%d: %s" % (i + 1, s))
        else:
            s = s[::-1]
            ans = ""
            while len(s) > 0:
                maxx = 0
                idx = 0
                for j in range(len(s)):
                    if s[j] > maxx:
                        maxx = s[j]
                        idx = j
                ans += maxx
                s = s[:idx] + s[idx+1:]
            print("Case #%d: %s" % (i + 1, ans))
    sys.stdout.close()
    sys.stdin.close()

threading.Thread(target = run).start()
