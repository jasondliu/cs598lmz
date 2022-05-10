import signal
# Test signal.setitimer function
def sig_handler(signum,frame):
    print("Received:",signum)

signal.signal(signal.SIGALRM,sig_handler)
signal.setitimer(signal.ITIMER_REAL,0.5,0.5)

while 1:
    print("Waiting...")
    time.sleep(1)

# 信号的配置,维护是一个全局的
# 信号和消息队列,管道,socket那些是没有先后关系的
