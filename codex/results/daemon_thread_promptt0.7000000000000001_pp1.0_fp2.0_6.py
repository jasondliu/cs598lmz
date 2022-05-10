import threading
# Test threading daemon
#
#

import time

def test():
    time.sleep(3)
    print "done."

if __name__ == '__main__':
    t = threading.Thread(target=test)
    t.setDaemon(True)
    t.start()
    print "main done."
