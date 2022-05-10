import threading
# Test threading daemon mode
#Note: Daemon thread means that when you exit the program all the daemon threads with the program
def DoCalc():
    for i in range(0,100000):
        print(i*5)

t = threading.Thread(target=DoCalc)
#t.setDaemon(True)
t.start()
print('end of program')
