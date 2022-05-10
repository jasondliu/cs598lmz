import signal
# Test signal.setitimer()
#   _thread.interrupt_main() ==> raise KeyboardInterrupt
#   _thread.interrupt_main() ==> raise KeyboardInterrupt
#   _thread.interrupt_main() ==> raise KeyboardInterrupt
#
import _thread
#
#
#
#
def handler(signum, frame):
    print("signal.setitimer() ==> raise KeyboardInterrupt")
    print("signal.setitimer() ==> raise KeyboardInterrupt")
    print("signal.setitimer() ==> raise KeyboardInterrupt")
    _thread.interrupt_main()
#
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, .5)
#
#
#
#
print("Test signal.setitimer()")
#
#
#
#
try:
    while True:
        print("Test signal.setitimer()")
        pass
except KeyboardInterrupt:
    print("\nGood bye!")
#
#
#
#
