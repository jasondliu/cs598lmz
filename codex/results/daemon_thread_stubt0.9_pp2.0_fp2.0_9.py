import sys, threading

def run():
    # TODO: Implement the function
    pass

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func, daemon=True)
    job_thread.start()

if __name__ == '__main__':
    run()
