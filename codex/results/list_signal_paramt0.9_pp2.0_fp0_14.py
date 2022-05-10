import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def printWithDelay(s):
    print(s)
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

with open("answers.txt") as f:
    next(f)
    for line in f:
        num, ans = line.strip().split('\t')
        ans = ans.replace(' ',',')
        call_str = "./check-dif -test "+ans+" -restrict "+num+".txt"
        correct = (subprocess.call(call_str.split(' '), timeout=2) == 0)
        printWithDelay("%s\t%s\t%s" % (num, "correct" if correct else "INCORRECT", ans))
