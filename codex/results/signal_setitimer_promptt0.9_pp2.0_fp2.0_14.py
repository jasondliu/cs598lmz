import signal
# Test signal.setitimer's ability to raise EINTR
if False:
    try:
        signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
        import time
        time.sleep(2) # Will reclaim the CPU after the CPU is available
    except:
        assert False, "setitimer interrupted"

# ---------------------------------------------------------------------------

# setitimer timeout should work in a multithreaded program
if hasattr(signal, 'alarm'):
    import thread
    import threading
    import time
    import os
    import pdb

    def thread1_sig(signum, frame):
        thread.start_new_thread(thread1_body, ())

    def thread1_body():
        global gotit
        gotit = 1
        time.sleep(0.1)

    def alarm_handler(signum, frame):
        print "alarm_handler called"

    signal.signal(signal.SIGALRM, thread1_sig)
    gotit = 0
    thread.start_new_thread(thread1_body
