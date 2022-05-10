import threading
# Test threading daemon
# https://stackoverflow.com/questions/30205851/python-is-it-possible-to-make-a-button-in-tkinter-tcl-tk-python-which-stop

# Base class for threads
class ThreadedTask(threading.Thread, object):
# Class variables shared by all instances
    thread_count = 0
    task_count = 0

    def __init__(self):
        super(ThreadedTask, self).__init__()
        ThreadedTask.thread_count += 1
        ThreadedTask.task_count += 1
        self.taskId = ThreadedTask.task_count
        # Create a unique interrupt event for this thread
        self.interrupt = threading.Event()
        print('Thread %d: Created interrupt event' % self.taskId)

    def cancel(self):
        print('Thread %d: Received a cancel event' % self.taskId)
        self.interrupt.set()

    def run(self):
        # Handle the input file
        while True:
            i_parsed = 0

