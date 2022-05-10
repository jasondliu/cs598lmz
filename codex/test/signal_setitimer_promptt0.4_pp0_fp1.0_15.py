import signal
# Test signal.setitimer()

def handler(num, frame):
    print('Alarm', num)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

for i in range(3):
    print('Waiting', i)
    time.sleep(1)

# Waiting 0
# Waiting 1
# Waiting 2
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Alarm 14
# Al
