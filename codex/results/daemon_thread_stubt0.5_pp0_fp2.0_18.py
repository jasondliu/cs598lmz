import sys, threading

def run():
    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.5)

threading.Thread(target=run).start()

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input('Enter number: '))
    if is_prime(n):
        print('Prime')
    else:
        print('Not Prime')

main()
</code>

