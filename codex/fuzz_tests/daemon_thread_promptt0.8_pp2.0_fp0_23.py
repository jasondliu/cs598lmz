import threading
# Test threading daemon
def th():
    print "This thread is daemon"
    time.sleep(1)
    print "Thread exit"

th_d = threading.Thread(target=th)
th_d.daemon = True
th_d.start()

print "Waiting child thread"
th_d.join()
print "Child thread exit"
