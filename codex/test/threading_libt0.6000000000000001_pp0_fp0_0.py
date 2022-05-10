import threading
threading.stack_size(67108864)

def find_nth_prime(n):
    found_prime = 0
    prime = 1
    while found_prime < n:
        prime += 1
        if is_prime(prime):
            found_prime += 1
    return prime

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def compute():
    n = 10001
    answer = find_nth_prime(n)
    return str(answer)


if __name__ == "__main__":
    print("Start")
    print("----------------------")
    start = time.time()
    answer = compute()
    end = time.time()
    print("----------------------")
    print
