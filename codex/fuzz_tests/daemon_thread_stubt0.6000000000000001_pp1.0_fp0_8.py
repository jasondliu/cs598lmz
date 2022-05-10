import sys, threading

def run():
    while True:
        try:
            if not read_key():
                break
        except KeyboardInterrupt:
            break

def read_key():
    return msvcrt.getch() != 'q'

thread = threading.Thread(target=run)
thread.start()

while thread.is_alive():
    try:
        sys.stdout.write(msvcrt.getch())
    except KeyboardInterrupt:
        break
</code>

