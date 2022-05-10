import threading
threading.stack_size(2**27)

# python3
def ModExp(x, y, N):
    if y == 0:
        return 1
    z = ModExp(x, int(y/2), N)
    if y % 2 == 0:
        return (z**2) % N
    else:
        return x * (z**2) % N
 
def main():
    print(ModExp(1777, 1855, 10**8))
 
thread = threading.Thread(target = main)
thread.start()
