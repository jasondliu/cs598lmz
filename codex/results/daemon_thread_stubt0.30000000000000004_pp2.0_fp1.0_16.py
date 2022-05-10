import sys, threading

def run():
    while True:
        try:
            print(input())
        except EOFError:
            sys.exit()

threading.Thread(target=run).start()

while True:
    try:
        print(input())
    except EOFError:
        sys.exit()
</code>

