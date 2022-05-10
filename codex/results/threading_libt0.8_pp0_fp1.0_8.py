import threading
threading.currentThread().name

if __name__ == '__main__':
    log_queue = Queue.Queue()
    log_listener = LogListener(log_queue)
    log_listener.start()

    try:
        for i in range(10):
            time.sleep(1)
            print log_listener.is_alive()
            if log_listener.is_alive():
                log_queue.put_nowait(i)
            else:
                break
        print "Exiting"
    finally:
        log_listener.stop()

    while True:
        try:
            print log_queue.get_nowait()
        except Queue.Empty:
            break
