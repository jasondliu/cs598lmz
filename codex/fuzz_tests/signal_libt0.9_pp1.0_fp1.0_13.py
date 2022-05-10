import signal
signal.signal(signal.SIGINT, sigint_handler)


class NumThreads:

    def __init__(self, max_threads, max_queue):
        self.max_threads = max_threads
        self.max_queue = max_queue
        self.thread_pool = ThreadPool(self.max_threads, self.max_queue)

    def start_threads(self):
        # populate inital jobs
        for i in range(1, self.max_threads + 1):
            start_time = time.time()
            self.thread_pool.add_job(self.thread_work, start_time)

        while self.thread_pool.working:
            time.sleep(1)

            if self.thread_pool.queue_full:
                start_time = time.time()
                self.thread_pool.add_job(self.thread_work, start_time)
                print("queue_full")

    @staticmethod
    def thread_work(start_time):
        print("Start Job")
        thread_
