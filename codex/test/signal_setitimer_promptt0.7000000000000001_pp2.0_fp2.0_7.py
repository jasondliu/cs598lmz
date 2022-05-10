import signal
# Test signal.setitimer to generate SIGALRM

def handle_alarm(signum, frame):
    print("Alarm!")

signal.signal(signal.SIGALRM, handle_alarm)

signal.setitimer(signal.ITIMER_REAL, 0.5)

while True:
    pass


## Try it with a timeout

#import signal
# Test signal.setitimer to generate SIGALRM

def handle_alarm(signum, frame):
    print("Alarm!")

signal.signal(signal.SIGALRM, handle_alarm)

signal.setitimer(signal.ITIMER_REAL, 0.5)

while True:
    pass


## Try it with a timeout

#import signal
# Test signal.setitimer to generate SIGALRM

def handle_alarm(signum, frame):
    print("Alarm!")

signal.signal(signal.SIGALRM, handle_alarm)

