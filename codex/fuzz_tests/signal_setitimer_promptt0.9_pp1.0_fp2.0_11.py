import signal
# Test signal.setitimer()

def handler(num, frame):
    print('Received signal', num)
    if num == signal.SIGALRM:
        print('Handling SIGALRM')
    else:
        print('Can only handle SIGALRM')

signal.siginterrupt(signal.SIGALRM, False)
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

try:
    while True:
        signal.pause()
except KeyboardInterrupt:
    print('Got ctrl-c')

# 可以发现，ctrl-c之后，pause()没有返回，直到sigalrm的处理函数被调用完成。
# 这是linux的行为，如果未挂起的信号不能被
