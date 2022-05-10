import sys, threading

def run():
    global mem
    while True:
        l = sys.stdin.readline().strip()
        if l == 'exit':
            return
        try:
            exec('global mem\n' + l)
            sys.stdout.write(repr(mem) + '\n')
        except Exception as e:
            sys.stdout.write('Error: ' + repr(e) + '\n')
        sys.stdout.flush()


if __name__ == "__main__":
    print "Starting repl"
    run()
