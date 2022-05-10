import threading
threading.stack_size(67108864) # 64MB stack

def is_prime(n):
    if n % 2 == 0:
        return False

