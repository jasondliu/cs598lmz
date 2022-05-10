import threading
threading.stack_size(64*1024)

def print_recursion(k):
    if (k > 0):
        print (k)
        print_recursion(k-1)
    else:
        threading.Thread(target=print_recursion, args=(1000000,)).start()

print_recursion(1000000)
