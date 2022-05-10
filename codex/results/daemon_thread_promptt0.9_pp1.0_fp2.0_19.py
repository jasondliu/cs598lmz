import threading
# Test threading daemonic and non daemonic

def worker_function(start_event):
    start_event.wait()
    for i in xrange(10):
        print "Worker: %d" % i
    print "Worker finishing"


def test_daemonic_threading(daemonic):
    w = threading.Thread(target=worker_function, daemon=daemonic)
    t0 = time.time()
    print "Starting worker"
    w.start()
    print "Waiting a little"
    time.sleep(5)
    print "Done waiting"
    print "Time: %.2fs" % (time.time() - t0)

# If a non-daemonic thread is still alive when the program exits, a
# message is written to the standard error and the process exits with
# a non-zero code.
test_daemonic_threading(daemonic=False)

# When the main thread exits, it wakes up all daemonic threads, which
# immediately exit, thus silent.
test_daemonic_threading(daemonic=True)
</
