import threading
threading.stack_size(67108864)

class GetData(threading.Thread):
    def __init__(self, threadID, name, q, q2):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
        self.q2 = q2

    def run(self):
        print("Starting " + self.name)
        while True:
            #print("Next Data\n")
            if (not self.q.empty()):
                #print("Started\n")
                #print("Queue Size: "+str(self.q.qsize()))
                #print("Queue 2 Size: "+str(self.q2.qsize()))
                #print("\n")
                curr_data = self.q.get()
                #print("Data: "+ curr_data)
                self.q2.put(curr_data)
                #print("Put Data\n")
                #print("Queue Size: "+str(self.q.qsize
