import select
# Test select.select() to see if it is able to read from stdin
# If not, then we will use the threaded version
try:
    select.select([sys.stdin], [], [], 0)
except:
    from select import select
    from threading import Thread
    from Queue import Queue
    from time import sleep

    def threaded_input(q):
        while True:
            q.put(sys.stdin.readline())

    def get_input(q):
        while True:
            read, write, error = select([sys.stdin], [], [], 0)
            if read:
                q.put(sys.stdin.readline())
            sleep(0.01)

    def get_user_input(threaded=False):
        q = Queue()
        if threaded:
            t = Thread(target=threaded_input, args=(q,))
            t.daemon = True
            t.start()
        else:
            t = Thread(target=get_input, args=(q,))
            t.daemon = True
