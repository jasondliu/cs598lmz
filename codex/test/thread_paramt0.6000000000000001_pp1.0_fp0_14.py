import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

def main():
    a = int(input())
    b = int(input())
    result = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            result += i
    print(result)
    
main()
