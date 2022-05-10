import sys, threading

def run():
    print("thread ", threading.current_thread())
    print(sys.argv)
    print("\n")
    
mythread = threading.Thread(target=run)
mythread.start()
print("I am the Main Thread here.\n")
