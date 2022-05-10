import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'.join('Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i) for i in range(1,101)))).start()

#Python 2.x
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print "FizzBuzz"
    elif i%3 == 0:
        print "Fizz"
    elif i%5 == 0:
        print "Buzz"
    else:
        print i

#Python 3.x
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

#Python 2.x
for i in range(1,101):
    print i%3/2*'Fizz'+i%5/4*'Buzz' or
