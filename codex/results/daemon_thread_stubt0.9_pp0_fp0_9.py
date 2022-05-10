import sys, threading

def run():
    global printer_queue, printer_lock
    while not printer_queue.empty():
        with printer_lock:
            queue_item = printer_queue.get()
            print "Thread[" + threading.currentThread().getName() + "]: " + queue_item
            sys.stdout.flush()
            time.sleep(1)

if __name__ == "__main__":
    problem_size = sys.argv[1]
    num_threads = sys.argv[2]
    printer_queue = Queue()
    printer_lock = threading.Lock()
    threads = []
    for i in range(int(num_threads)):
        new_thread = threading.Thread(target=run)
        threads.append(new_thread)
        new_thread.start()
    for i in range(int(problem_size)):
        printer_queue.put(str(i))
    for thread in threads:
        thread.join()
    print "Job finished!"
