import threading
# Test threading daemon status
def daemon():
    print("starting daemon")
    time.sleep(1000)
    print("end daemon")
    
daemon_job = threading.Thread(target=daemon)
daemon_job.setDaemon(True) # default True
daemon_job.start()
daemon_job.isDaemon()

daemon_job.is_alive()

# output:
"""
starting daemon
end daemon
"""
# Test threading join() before main thread end.
def worker():
    print("starting worker")
    time.sleep(10)
    print("end worker")

worker_job = threading.Thread(target=worker)
worker_job.start()

# worker_job.run() # No effect.
worker_job.join() # main thread is blocked.
print("main thread ends.")

# output:
"""
starting worker
end worker
main thread ends.
"""
# Test threading join() after main thread end.
def worker():
    print("starting worker")
    time.sleep(10)
    print("end worker")
