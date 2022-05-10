import sys, threading

def run():
    while True:
        try:
            s = raw_input()
        except KeyboardInterrupt:
            break
        if not s:
            break
        try:
            sys.stdout.write('%d\n' % int(s) ** 2)
            sys.stdout.flush()
        except ValueError:
            sys.stdout.write('INVALID\n')
            sys.stdout.flush()
    sys.exit(0)

thread = threading.Thread(target=run)
thread.start()

while thread.is_alive():
    try:
        thread.join(1)
    except KeyboardInterrupt:
        break

sys.exit(0)
