import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print('end')

def sortn(n):
	#this function sorts the natural numbers in a list
	# it uses a sort algorithm that is faster than mergesort
	# it returns a sorted copy of the input
	#the input is a list of natural numbers
	#the only way to do it will be to make a list of lists to put the numbers in
	
	# this works by putting numbers into lists
	# the lists are organized by their value modulus the length of the list
	# this is because a large number modulus a small number will always be smaller
	# than a smaller number modulus a larger number
	
	#example: when the list is length 2, it is organized by odd and even
	#example: when the list is length 3, it is organized by 0,1 and 2 modulus 3

	#this is one of the most advanced functions that I have made in python
	
	tl = []
	for x in range(len(n)):
		tl.append([])
	for x in n:
		tl[x % len(n)].append(x)

