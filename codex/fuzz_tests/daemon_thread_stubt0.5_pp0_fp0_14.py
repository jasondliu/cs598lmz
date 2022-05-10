import sys, threading

def run():
    while True:
        try:
            exec(input())
        except EOFError:
            exit(0)

t = threading.Thread(target=run)
t.daemon = True
t.start()

while True:
    try:
        print(eval(input()))
    except EOFError:
        exit(0)
</code>

