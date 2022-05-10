import threading
# Test threading daemon
def printSome():
    while True:
        data = input("Enter something: ")
        print(data)

def serverRun():
    startThreads = threading.Thread(target=printSome)
    startThreads.daemon = True
    startThreads.start()
    #startThreads.join()

serverRun()
</code>
The program never gets to <code>serverRun()</code> if I add <code>startThreads.join()</code>. And if I don't add <code>startThreads.join()</code> I have to create a loop for the user input in order for the prompt to show up again. Or the program will just finish and close


A:

When you use <code>join()</code>, it waits for the thread to finish before continuing. In your case, the thread you are waiting on is the thread that takes user input, which will never finish, because it's waiting for user input.

