import threading
threading.stack_size(2 ** 27)

# Create a class to handle threading
class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()


# Create a class to handle the data processing
class DataProcessing(StoppableThread):
    def __init__(self, data_queue, stop_flag, process_data_callback):
        super(DataProcessing, self).__init__()
        self.data_queue = data_queue
        self.stop_flag = stop_flag
        self.process_data_callback = process_data_callback

