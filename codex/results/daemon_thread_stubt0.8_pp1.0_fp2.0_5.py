import sys, threading

def run():
    sys.stdout.write('\n')
    sys.stdout.write('Listen to input ...\n')
    sys.stdout.write('Press CTRL + Z\n')
    while True:
        try:
            a = sys.stdin.readline()
            print(a)
        except KeyboardInterrupt:
            sys.stdout.write('\n')
            sys.stdout.write('Have a good day\n')
            sys.stdout.write('\n')
            break
        except:
            pass

thread = threading.Thread(target=run)
thread.start()
