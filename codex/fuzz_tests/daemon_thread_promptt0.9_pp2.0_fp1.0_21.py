import threading
# Test threading daemon
import time
class CommandThread(threading.Thread):
    sequence_number=0
    def __init__(self,func,*arg):        
        #threading.Thread.__init__(self)
        super().__init__()#py3 syntax for py2 need use super(CommandThread,self).__init__()
        self.func=func
        self.arg=arg
        self.sequence_number=CommandThread.sequence_number
        CommandThread.sequence_number+=1
        self.thread_id=threading.get_ident()

    def __del__(self):
        print("thread {},{} deleted".format(self.sequence_number,se
