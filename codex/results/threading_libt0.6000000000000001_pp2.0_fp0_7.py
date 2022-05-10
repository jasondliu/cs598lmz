import threading
threading.stack_size(67108864)  # 64MB stack

def run_thread(name):
    print(name)
    return

for i in range(5):
    t = threading.Thread(target=run_thread, args=(i,))
    t.start()
