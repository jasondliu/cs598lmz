import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from a thread!\n')).start()

#A reference to a thread can be used to determine if it is still running and to wait for the thread to finish its execution.
def thread_target(L):
    for i in range(len(L)): L[i] += 1
storage = [1, 2, 3, 4, 5]
threading.Thread(target=thread_target, args=(storage,)).start()
#The previous code starts a new thread of execution and gives it a reference to a list L. 
#The thread will then add 1 to each element in the list. The thread has started executing, 
#but the main thread continues running.
print(storage)
#[1, 2, 3, 4, 5]
#At this point, the other thread has probably finished executing the for loop. The changes that it 
#made are not visible to the main thread until the thread has exited.
#We can examine the output from the other thread by looking at the reference to the thread object
x = threading.Thread(target=thread_target, args=(storage,))

