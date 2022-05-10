import threading
# Test threading daemon
def run_jobs_thread(jobs, n_threads, daemon=True):
    threads = [threading.Thread(target=job) for job in jobs]
    for thread in threads:
        thread.daemon = daemon
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
def run_jobs_thread_no_daemon(jobs, n_threads):
    threads = [threading.Thread(target=job) for job in jobs]
    for thread in threads:
        thread.daemon = False
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
# Run jobs without daemon mode
import time
start = time.time()
run_jobs_thread(jobs, 2)
print("Elapsed time using threads =",time.time()-start)

start = time.time()
run_jobs_thread_no_daemon(jobs, 2)
print("Elapsed time using threads no daemon =",time.time()-start)
print('\n
