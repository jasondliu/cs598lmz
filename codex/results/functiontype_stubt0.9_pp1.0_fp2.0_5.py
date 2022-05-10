from types import FunctionType
a = (x for x in [1])
type(a)

print('Time in seconds since the epoch: %s' %time.time())
print('Current date and time: %s' %datetime.datetime.now())
print('Or like this: %s/%s/%s' % (now.year, now.month, now.day))
print('Hoy es %s' % now)

for i in range(1,10):
    if i%3==0:
        print("Fizz")
    if i%5==0:
        print("Buzz")
    else:
        print(i)
        
def fizz_buzz1(x):
    for i in range(0,x):
        if i % 3 == 0: 
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def fizz_buzz2(x):
    for i in range(0,x):
        os = ''

