import mmap

def findItem(sl, lst, item):
	if lst[sl] == item:
		return sl
	elif lst[sl] < item:
		return findItem(sl+1, lst, item)
	elif lst[sl] > item:
		return findItem(sl-1, lst, item)



def main():
	l = [10,20,30,40,50,60,70,80]
	target = 100
	r = findItem(len(l)-1, l, target)
	print r



if __name__ == '__main__':
	main()
