import signal
# Test signal.setitimer() in subprocesses
def alarm_handler(signum, frame):
    print("Hello, World!\n")
    signal.setitimer(signal.ITIMER_REAL, 0.5)

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
while True:
    time.sleep(2)
"""

import subprocess

cmd = ['python', '-c', code]
with subprocess.Popen(cmd,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.STDOUT,
                      bufsize=0) as p:
    for line in p.stdout:
        print(line.decode(encoding='utf-8').rstrip())
    p.wait()
