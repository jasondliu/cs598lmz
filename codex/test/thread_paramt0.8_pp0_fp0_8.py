import sys, threading
threading.Thread(target=lambda: sys.stdout.write('{{}}'.format(sys.stdin.readline())))

2^31+3333

x=5
y=5

if x==y:
    print(str(x) + ' is equal to ' + str(y))
if x<y:
    print(str(y) + ' is greater than ' + str(x))
if x>y:
    print(str(y) + ' is less than ' + str(x))

x=5
y=5

if x==y:
    print(str(x) + ' is equal to ' + str(y))
elif x<y:
    print(str(y) + 'is greater than ' + str(x))
else:
    print(str(y) + 'is less than ' + str(x))
    
    
def xyz(a,b,c=10,*d):
    print(a,b,c,d)
xyz(1,2,3,4,5,6,7)

