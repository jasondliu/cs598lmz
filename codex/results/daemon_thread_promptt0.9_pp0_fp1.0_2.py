import threading
# Test threading daemon
def longdaemon_loop(count=1000, id=0, run_event=threading.Event()):
    while not run_event.is_set():
        print('long daemon', id)
        time.sleep(1)

if __name__=='__main__':
    run_event = threading.Event()
    for i in range(3):
        t = threading.Thread(target=longdaemon_loop,
                            args=(10, i),
                            kwargs={'run_event': run_event})
        t.setDaemon(True)
        t.start()

    run_event.set()
    time.sleep(5)
