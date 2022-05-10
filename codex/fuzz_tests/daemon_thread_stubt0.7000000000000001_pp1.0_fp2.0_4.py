import sys, threading

def run():
    global queue
    # gets the queue from the global namespace
    while not queue.empty():
        # runs the loop until there are no more items in the queue
        print(queue.get())
        # prints the contents of the queue
        queue.task_done()
        # removes the item from the queue

queue = Queue.Queue()
# creates a queue object

for i in range(10):
    # runs the loop 10 times
    queue.put("Message " + str(i))
    # puts the string in the queue

for i in range(5):
    # runs the loop 5 times
    t = threading.Thread(target=run)
    # creates a thread object, using the target function run
    t.daemon = True
    # sets the daemon property of the thread to True
    t.start()
    # starts the thread

queue.join()
# waits for all of the items in the queue to be processed
</code>
As you can see, the queue is global so it can be accessed by all of the threads.
Hope this helps!

