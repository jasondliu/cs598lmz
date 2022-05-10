import sys, threading

def run():
    while True:
        try:
            cmd = sys.stdin.readline()
            if cmd == '':
                break
            if cmd.startswith('/'):
                continue
            print(cmd)
        except:
            break

thread = threading.Thread(target=run)
thread.start()

while True:
    try:
        print(sys.stdin.readline())
    except:
        break
</code>

