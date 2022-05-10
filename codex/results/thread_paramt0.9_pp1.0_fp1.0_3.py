import sys, threading
threading.Thread(target=lambda: stdin.readlines()).start()

def decode(string,base):
    res = 0
    for s in string:
        val = ord(s)
        if ord('a') <= val <= ord('z'):
            res = res * base + val - ord('a')
        elif ord('A') <= val <= ord('Z'):
            res = res * base + val - ord('A')
        elif ord('0') <= val <= ord('9'):
            res = res * base + val - ord('0') + 36
        elif val == ord('+'):
            res = res * base + 62
        elif val == ord('/'):
            res = res * base + 63

    return res

cases = 0
flag = False
while True:
    try:
        if flag:
            stdout.write("\n")
        cases += 1
        flag = True
        stdout.write("Case %d:\n"%cases)
        base = int(stdin.readline())

        line = stdin.readline()
       
