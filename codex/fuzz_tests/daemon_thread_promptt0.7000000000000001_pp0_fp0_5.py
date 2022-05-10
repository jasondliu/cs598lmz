import threading
# Test threading daemon
def first_thread():
    print threading.current_thread()
    print "First thread start"
    time.sleep(5)
    print "First thread end"

def second_thread():
    print threading.current_thread()
    print "Second thread start"
    time.sleep(5)
    print "Second thread end"

if __name__ == '__main__':
    t1 = threading.Thread(target=first_thread)
    t2 = threading.Thread(target=second_thread)
    t1.start()
    t2.start()
    print threading.current_thread()
