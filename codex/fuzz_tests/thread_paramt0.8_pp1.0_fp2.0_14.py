import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hey!\n')).start()
'''

class HelloWorld(threading.Thread):
    def run(self):
        for i in range(5):
            print("Hello!")
            sleep(1)

class SupWorld(threading.Thread):
    def run(self):
        for i in range(5):
            print("Sup!")
            sleep(1)
            
t1 = HelloWorld() 
t2 = SupWorld()

t1.start()
t2.start()
t1.join()
t2.join()
