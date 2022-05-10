import threading
# Test threading daemon
# Iterates to the number of 0.5 seconds specified in the sleep call and outputs the text specified.
print("Creating thread.")
thread1 = threading.Thread(target=testThread,args=("testThread_1\n",))
thread1.daemon = False
thread1.start()

print("\nthread1.daemon:")
print(thread1.isDaemon())

print("\nthread1.isAlive():")
print(thread1.isAlive())

print("\nthread1.name:")
print(thread1.getName())
 
#Changes the name of the thread1
print("\nAssigning name to thread1.")
thread1.setName("testThread_1")

#Returns the name of the thread1
print("\nthread1.name:")
print(thread1.getName())

print("\nthread1.isDaemon():")
print(thread1.isDaemon())

print("\nthread1.isAlive():")
print(thread1.isAlive())

print("\nthread
