import threading
# Test threading daemon
def target_func(sleep_time):
    print "target_func begin %s" % sleep_time
    time.sleep(sleep_time)
    print "target_func end %s" % sleep_time

def run():
    print "main begin"
    t1 = threading.Thread(target=target_func, args=[5])
    t1.start()
    print "main end"

run()
print "Done!"
