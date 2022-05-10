import threading
threading.stack_size(67108864)

def hello():
    print('Hello from thread!')

t = threading.Thread(target=hello)
t.start()
