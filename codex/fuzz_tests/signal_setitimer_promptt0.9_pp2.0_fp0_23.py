import signal
# Test signal.setitimer()

# 本函数内部就是核心内容
def alarm_received(n, stack):
    return and then what?

signal.signal(signal.SIGALRM, alarm_received)

signals_to_names = {}
for n in dir(signal):
    if n.startswith('SIG') and not n.startswith('SIG_'):
        signals_to_names[getattr(signal, n)] = n

# 本函数只是辅助
def watch_for_alarm(n):
    while True:
        sig = signal.sigwait([signal.SIGALRM])
        print('ALARM', signals_to_names[sig])

# 具体的执行
if __name__=='__main__':
    import os
    alarm_thread = threading.Thread(
        target=watch_for_alarm,
        name='alarm_thread',
        args=(),

