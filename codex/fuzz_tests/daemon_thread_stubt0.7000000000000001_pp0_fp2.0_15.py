import sys, threading

def run():
	n = int(input().strip())
	arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
	s = 0
	for i in range(n):
		s += arr[i]
	print(s)

t = threading.Thread(target=run)
t.start()
