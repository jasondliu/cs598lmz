import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.signal(signal.SIGALRM, alarm_handler)

# Test signal.setitimer()
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
signal.signal(signal.SIGPROF, prof_handler)

for i in range(1, 20):
    print('loop at', i)
    time.sleep(0.01)

signal.setitimer(signal.ITIMER_REAL, 0)
signal.setitimer(signal.ITIMER_PROF, 0)

# 设置信号的处理函数
# signal.signal(signal.SIGINT, signal_handler)

# if __name__ == '__main__':
#     # input()
#     time.sleep(10)
