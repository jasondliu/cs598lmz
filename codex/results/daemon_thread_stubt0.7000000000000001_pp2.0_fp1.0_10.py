import sys, threading

def run():
    for i in range(1000):
        print(i, end=" ")


print(__name__)

if __name__ == '__main__':
    run()
