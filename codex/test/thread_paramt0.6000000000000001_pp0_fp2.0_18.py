import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join('Fizz'*(not i%3)+'Buzz'*(not i%5) or str(i) for i in xrange(1,101)))).start()


# One-line solution (Python 3.x)
exec('print("\n".join(["FizzBuzz"[i*i%3*4:8--i**4%5]or`i`for i in range(1,101)]))')


# One-line solution (Python 3.x)
