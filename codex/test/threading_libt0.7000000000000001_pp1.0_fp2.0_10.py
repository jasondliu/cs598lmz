import threading
threading.stack_size(67108864) # 64MB stack

N = 4

def run_thread(in_val):
    sum = 0
    for i in range(N):
        sum += i

    for i in range(N):
        sum += i

