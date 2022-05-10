import signal
# Test signal.setitimer()
def handler(num, frame):
    print('Alarm', num)
    print(frame)

alarm_num = signal.SIGALRM
signal.signal(alarm_num, handler)
signal.setitimer(alarm_num, 2)
time.sleep(10)
print('Done')
