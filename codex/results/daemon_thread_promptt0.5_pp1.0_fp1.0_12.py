import threading
# Test threading daemon

def my_thread():
    print "threading start!"
    time.sleep(5)
    print "threading end!"

my_thread = threading.Thread(target = my_thread)
my_thread.daemon = True
my_thread.start()

print "Main Thread"

# Test threading not daemon

def my_thread2():
    print "threading start!"
    time.sleep(5)
    print "threading end!"

my_thread2 = threading.Thread(target = my_thread2)
my_thread2.daemon = False
my_thread2.start()

print "Main Thread"

# Test threading daemon

def my_thread3():
    print "threading start!"
    time.sleep(5)
    print "threading end!"

my_thread3 = threading.Thread(target = my_thread3)
my_thread3.daemon = True
my_thread3.start()

print "Main Thread"
