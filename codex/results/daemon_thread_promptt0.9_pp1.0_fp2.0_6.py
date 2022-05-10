import threading
# Test threading daemon 
# https://docs.python.org/2/library/threading.html#thread-objects
# https://stackoverflow.com/questions/323972/is-there-anyway-to-kill-a-thread-in-python
class Drive(threading.Thread):
    def __init__(self, threadID, name, counter, motor_left, motor_right):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.motor_left = motor_left
        self.motor_right = motor_right

    def run(self):
        print ("run start : " + self.name)
        print_time(self.name, self.counter)
        print ("run end : " + self.name)

    def loop(self):
        while(1):
            if(1==1):
                self.motor_left.drive(0)
                self.motor_righr.drive(0)
            else:
                self.m
