import sys, threading
threading.Thread(target=lambda: sys.stdin.readline()).start()

def main():
    N = int(sys.stdin.readline().strip())
    for i in range(1, N + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

main()
