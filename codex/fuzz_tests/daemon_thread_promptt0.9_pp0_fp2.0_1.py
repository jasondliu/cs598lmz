import threading
# Test threading daemon
# import queue
class TestDaemon(threading.Thread):
    def __init__(self, taskQueue):
        threading.Thread.__init__(self)
        self.a = 1
        self.b = 1
        self.taskQueue = taskQueue

    def run(self):
        while True:
            if not self.taskQueue.empty():
                task = self.taskQueue.get()
                if task.cmd == "updatea":
                    self.a = task.aVal
                elif task.cmd == "updateb":
                    self.b = task.bVal
                elif task.cmd == "get":
                    taskQueue.put(self.a + self.b)

            

taskQueue = Queue()
testDaemon = TestDaemon(taskQueue)
testDaemon.daemon = True
testDaemon.start()
for i in range(1, 100):
    taskQueue.put(Task("updatea", i))
    taskQueue.put(Task("updateb", i+1))
    taskQueue.put(Task("get"))

