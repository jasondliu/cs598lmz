import threading
# Test threading daemonization
# To use this script, make sure to send SIGUSR1 signal to the process.
# Example: kill -s SIGUSR1 `pidof py`
#
# Note that the script might need to be run twice.
# On the first run, warning will be printed:
# "OSError: [Errno 9] Bad file descriptor"

thread_names = {}
def test_fn(name):
    # Print threads info
    thread_names[threading.get_ident()] = name
    print ("%s: %s" % (name, threading.enumerate()))

    # Wait for SIGUSR1
    # On the first run, an error might occur: "OSError: [Errno 9] Bad file descriptor"
    # This error can be ignored
    signal.pause()

def sigusr1_handler(signum, frame):
    thread_id = threading.get_ident()
    print ("Received signal in %s (%d)" % (thread_names[thread_id], thread_id))

if __name__ == '__main__':

