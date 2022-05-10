import threading
threading.stack_size(67108864) # 64MB stack

def my_function():
    print("Hello from a thread!")

t = threading.Thread(target=my_function)
t.start()
