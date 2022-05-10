import threading
threading.Thread(target=lambda: print("hi")).start()



from threading import Thread
def task1(name):
    Thread(target=task2).start()
    print(name)
    
def task2():
    print("World")
    
task1("hello")



from threading import Thread
Thread(target=lambda: print("hello")).start()
print("World")


from threading import Thread
def task1():
    print("World")

Thread(target=task1).start()
print("hello")


from threading import Thread
def task1(name):
    Thread(target=task2).start()
    print(name)
    
def task2():
    print("World")
    
task1("hello")



from threading import Thread
def task1():
    print("World")

Thread(target=task1).start()
print("hello")


from threading import Thread
def task1(name):
    Thread(target=task2).start()
    print(name)
    
def task2():
   
