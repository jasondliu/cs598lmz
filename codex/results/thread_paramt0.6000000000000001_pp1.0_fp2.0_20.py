import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join('Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i) for i in range(1, int(sys.argv[1])+1)))).start()
