import threading
# Test threading daemon (can see threads still running after program finishes)
# If deamon == True it runs in the background

# Command for testing:
# python2 ~/Dropbox/Work/gps/test_threadingDaemon.py
def sleeper(i):
    print("thread {} sleeping for 5 seconds".format(i))
    time.sleep(5)
    print("thread {} woke up".format(i))

for i in range(10):
    t = threading.Thread(target=sleeper, args=(i,))
    t.daemon = True
    t.start()

print("Main thread done")
