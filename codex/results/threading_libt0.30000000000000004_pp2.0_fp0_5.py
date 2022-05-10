import threading
threading.stack_size(67108864)

def check_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def main():
    number = 600851475143
    i = 2
    while i * i < number:
        while number % i == 0:
            number = number / i
        i = i + 1
    print(number)

thread = threading.Thread(target=main)
thread.start()
