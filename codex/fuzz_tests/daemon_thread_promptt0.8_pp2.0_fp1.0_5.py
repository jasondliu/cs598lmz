import threading
# Test threading daemon with sklearn
while True:

    th = threading.Thread(target=dummy_function)
    th.daemon=True #set daemon to True so the thread dies together with the main thread
    th.start()
    # time.sleep(10)
    print "Thread %s is alive: %s" % (th.getName(), th.is_alive())
    print "Current thread is %s" % threading.current_thread().getName()

# How to print out results from multiprocessing?
import numpy as np
from time import sleep
import multiprocessing
from multiprocessing import Pool, cpu_count

# Model code
class model_instance(object):
    def __init__(self, name, random_variables):
        self.name = name
        self.random_variables = random_variables

    def run_model(self):
        # Run the model
        output = np.dot(self.random_variables, 2.0)
        return output

# Main
if __name__ == '__main__':

    num
