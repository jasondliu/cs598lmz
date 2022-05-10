import signal
# Test signal.setitimer
import time

def alarm_handler(signum, frame):
    if p.poll():
        p.kill()

p = subprocess.Popen(["python", "-c", "import time; time.sleep(10)"])
signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

# Test signal.reentrant
import subprocess
# This test passes if we don't hangs or crash
subprocess.call(["python", "-c", 'import signal; signal.signal(signal.SIGALRM, signal.SIG_IGN)'])

# Tests for keyword args to the subprocess functions
import subprocess
def call(*args, **kwargs): pass
def check_call(*args, **kwargs): pass
def check_output(*args, **kwargs): pass
def Popen(*args, **kwargs): pass
for obj in [subprocess.call, subprocess.check_call, subprocess.check_output, subprocess.Popen]:
   
