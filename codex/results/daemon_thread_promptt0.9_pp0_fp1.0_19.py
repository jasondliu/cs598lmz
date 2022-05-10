import threading
# Test threading daemon function/////////////////////////////////////////////
# Test threading daemon function/////////////////////////////////////////////

class SendThread(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self, name=threadName)
    def run(self):
        global name
        global clientPort
        global clientSocket
        global nameList
        global dictList
        global userNum
        global dict
        global lock
        global flag_this
        print('thread %s id running...' % threading.current_thread().name)
        if lock.acquire():
            if(flag_this ==1):
                dict = {'name':name,'dictList':dictList,'userNum':userNum+1}
            else:
                dict = {'name':name,'dictList':dictList,'userNum':userNum}
            lock.release()
        while True:
            if(flag_this == 1):
                clientSocket.sendto(pickle.dumps(dict), (clientHost, clientPort))
                flag_this = 0
#            sendBuf = input()
