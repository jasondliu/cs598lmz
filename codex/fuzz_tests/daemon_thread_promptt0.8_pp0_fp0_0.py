import threading
# Test threading daemon for periodically printing the CPU temperature to the console.
class CpuTempThread(threading.Thread):
    # Constructor
    def __init__(self):
        self.runout = False
        threading.Thread.__init__(self)

    # Overrides the run method of threading.Thread to specify what runs in the thread.
    def run(self):
        while not self.runout:
            time.sleep(1)
            sys.stdout.write("\rCPU Temperature: {}".format(getCPUTemp()))
            sys.stdout.flush()
    # Kill the thread.
    def kill(self):
        self.runout = True

# Test main that spawns a thread to print the CPU temperature.
def main():
    print("Test main that spawns a thread to print the CPU temperature.")
    cpuTempThread = CpuTempThread()
    cpuTempThread.start()
    try:
         while True:
             time.sleep(0.1)
    except KeyboardInterrupt:
        cpuTempThread.kill()
        cpuTempThread.join()
       
