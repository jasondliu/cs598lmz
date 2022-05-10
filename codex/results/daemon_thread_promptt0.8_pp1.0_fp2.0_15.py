import threading
# Test threading daemon
def daemon():
    #pid = os.getpid()
    print("starting daemon")
    sys.stdout.flush()
    while True:
        #print("daemon doing something")
        #sys.stdout.flush()
        time.sleep(1)


# Main

if __name__ == "__main__":
    print("starting")
    sys.stdout.flush()
    thread = threading.Thread(target = daemon)
    thread.setDaemon(True)
    thread.start()
    time.sleep(2)
    print("exiting")
    sys.stdout.flush()

</code>
Output:
<code>starting
starting daemon
exiting

</code>
Seems daemon thread is not working. It is actually working in other non-daemon threads.
Environment:
<code>$ python3 -V
Python 3.7.3
</code>
I'm trying to get a better understanding of the Python threading module.


A:

<blockquote>
<p>Seems daemon thread is not working. It is actually
