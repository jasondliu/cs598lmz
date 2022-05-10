import ctypes
import ctypes.util
import threading
import sqlite3
import csv
import sys
import signal

# init
conf_file = None
conf_db = None
process_list = []
lock = threading.Lock()

def signal_handler(signal, frame):
    print "SIGINT caught, terminating gracefully"
    print "Terminating processes:"
    for p in process_list:
        try:
            print "Terminating process %d" % p.pid
            p.terminate()
        except OSError, e:
            print "Error while terminating process %d: %s" % (p.pid, e.strerror)
    print "Done!"
    sys.exit(0)

if __name__ == "__main__":

    signal.signal(signal.SIGINT, signal_handler)

    # parse arguments
    if len(sys.argv) != 2:
        print 'Usage: %s conf_file' % (os.path.basename(sys.argv[0]))
        sys.exit(1)
    conf_file = sys.argv[1]
