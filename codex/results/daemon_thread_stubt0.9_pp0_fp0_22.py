import sys, threading

def run():
    n = 1
    for l in sys.stdin:
        t = l
        # print t
        if len(l) == 0:
            break;
        t = l[len(l)-2]
        if t == ' ':
            pass
        elif t == '-':
            n -= 1
        elif t == '+':
            n += 1
        elif t == '4':
            n += l.count('4')
            n += l.count('7')
        elif t == '7':
            n += l.count('4')
            n += l.count('7')
    print n

t = threading.Thread(target = run)
t.start()
t.join()
