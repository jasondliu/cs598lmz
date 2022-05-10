import threading
# Test threading daemon.
# Threading daemon, standard methods are start, join and is_alive.
# The daemon thread will finish when the main program exits.
# Threading has a Timeout, which is None by default, but you can set it to anything.
def fun():
    print ('Hello threading!')
    time.sleep(1)
    print ('Bye threading')

thread_one = threading.Thread(name='thread_one', target=fun)
# thread_one.setDaemon(True)
# The main thread exits.
# The threading daemon exits because the main thread exited.
thread_one.start()
time.sleep(2)
print ('is_alive thread_one: {}' .format(thread_one.is_alive()))
print ('Main program done')
# thread_one.join()

# thread_one.join(2)
# thread_one.join(1)
