import threading
# Test threading daemon

def do_so_thread():
    print('Hello')
    time.sleep(2.0)
    print('World')


my_thread = threading.Thread(target=do_so_thread, daemon=True)
my_thread.start()

print('Waiting for something...')



# Message passing - producer consumer queue
import queue

my_queue = queue.Queue(maxsize=20)

def consumer(queue):
    while True:
        item = queue.get()
        if item is 'quit':
            break
        print('Consumed', item)
        queue.task_done()
    print('Queue consuming complete')

def producer(queue):
    for i in range(10):
        queue.put(i)
        print('Produced', i)
    queue.put('quit')
    print('Queue producing complete')

producer_thread = threading.Thread(target=producer, args=(my_queue, ))
consumer_thread = threading.Thread(target=consumer, args=(my_queue, ))

producer_thread.
