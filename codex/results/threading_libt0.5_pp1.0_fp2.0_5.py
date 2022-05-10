import threading
threading.stack_size(512*1024)
sys.setrecursionlimit(2**20)

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def main():
    n = int(input())
    if n == 1:
        print("Not prime")
        return
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")

thread = threading.Thread(target=main)
thread.start()
