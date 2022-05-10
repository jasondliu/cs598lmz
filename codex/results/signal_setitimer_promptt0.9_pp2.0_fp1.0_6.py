import signal
# Test signal.setitimer()
print(time.ctime())
# signal.alarm(5)  # 开始计时, 而且设置信号时间, 在5秒后会发送SIGALRM信号
signal.signal(signal.SIGALRM, lambda signum, frame: print('SIGALRM'))
# 第一个参数: 指定要处理的信号, 第二个参数: 要执行的处理函数
signal.setitimer(signal.ITIMER_REAL, 3, 1)  # 从调用开始计时器开始计时, 在3秒以后发送信号, 每隔1秒发送一次信号
