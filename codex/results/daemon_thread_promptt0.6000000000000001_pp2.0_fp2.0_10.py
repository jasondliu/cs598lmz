import threading
# Test threading daemon
def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.daemon = True
    job_thread.start()
    return job_thread

def read_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.daemon = True
    job_thread.start()
    return job_thread

def write_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.daemon = True
    job_thread.start()
    return job_thread
# Test threading daemon


# device_monitor
def device_monitor(device):
    def dev_mon():
        dev_monitor = DeviceMonitor(device)
        dev_monitor.run()

    return dev_mon

# device_monitor


# Read device
def read_device(device):
    def read_dev():
        dev_read = DeviceRead(device)
        dev_read.run()


