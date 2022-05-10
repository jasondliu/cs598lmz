import threading
threading.stack_size(67108864)

def is_prime(n):
    if n % 2 == 0:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def main():
    T=int(input())
    for _ in range(T):
        n=int(input())
        if (n==1):
            print("Not prime")
            continue
        if (n==2):
            print("Prime")
            continue
        if (n%2==0):
            print("Not prime")
            continue
        print("Prime" if is_prime(n) else "Not prime")

thread = threading.Thread(target=main)
thread.start()
