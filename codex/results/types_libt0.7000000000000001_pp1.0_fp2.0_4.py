import types
types.ListType

#
def printMax(x,y):
	'''Prints the maximun of two numbers.

	The two values must be integers.'''
	x = int(x)
	y = int(y)
	
	if x > y:
		print x,'is maximum'
	else:
		print y,'is maximum'
printMax(3,5)
print printMax.__doc__

#
def say(message,times=1):
	print message * times
say('Hello')
say('Hello',5)

#
def func(a,b=5,c=10):
	print 'a is',a,'and b is',b,'and c is',c
func(3,7)
func(25,c=24)
func(c=50,a=100)

#
def total(initial=5,*numbers,**keywords):
	count = initial
	for number in numbers:
		count += number
	for key in keywords:
		count += keywords[key]
	return count
print total
