import signal
# Test signal.setitimer() with SIGCHLD

def handler(signo, frame):
    print("signal", signo, "caught")

signal.signal(signal.SIGCHLD, handler)

pid = os.fork()

if pid == 0:
    # child
    print("child")
    os._exit(0)

itimer_type = signal.ITIMER_REAL
interval = 5
print("parent", pid)

signal.setitimer(itimer_type, interval, 0)
print("parent waiting")
reaped, status = os.waitpid(pid, 0)
print("child reaped", reaped, status)
signal.setitimer(itimer_type, 0)

# just to keep the output on the screen
input("End")
