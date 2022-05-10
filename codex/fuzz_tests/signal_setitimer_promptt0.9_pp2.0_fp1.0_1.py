import signal
# Test signal.setitimer
numer_of_halt = 0


def handle_timeout(signum, frame):
    global numer_of_halt
    numer_of_halt += 1
    print numer_of_halt


signal.signal(signal.SIGALRM, handle_timeout)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)  # 进程维持一个时间计数器，每隔一段时间将定时器清零，并发出信号

try:
    while 1:
        sys.stdout.flush()
        time.sleep(1)
except KeyboardInterrupt:
    print numer_of_halt
    signal.setitimer(signal.ITIMER_REAL, 0)  # 进程维持一个时间计数
