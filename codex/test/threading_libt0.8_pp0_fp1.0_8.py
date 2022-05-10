import threading
threading.currentThread().name

if __name__ == '__main__':
    log_queue = Queue.Queue()
    log_listener = LogListener(log_queue)
    log_listener.start()

