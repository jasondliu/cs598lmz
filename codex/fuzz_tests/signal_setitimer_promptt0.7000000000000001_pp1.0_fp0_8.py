import signal
# Test signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

def start():
    signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

def stop():
    signal.setitimer(signal.ITIMER_PROF, 0, 0)

def handler(signum, frame):
    print "Profiler tick"

def main():
    signal.signal(signal.SIGPROF, handler)
    start()
    raw_input("Type anything to stop profiling: ")
    stop()

if __name__ == '__main__':
    main()
</code>

