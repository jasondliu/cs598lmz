import sys, threading

def run():
    run_event.set()
    t1 = threading.Thread(target=do_something)
    t2 = threading.Thread(target=do_something)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def do_something():
    print("Thread {} starting".format(threading.current_thread().name))
    run_event.wait()
    while run_event.is_set():
        pass
    print("Thread {} ending".format(threading.current_thread().name))

def stop():
    run_event.clear()

run_event = threading.Event()

run()
run()
run()

# EOF
