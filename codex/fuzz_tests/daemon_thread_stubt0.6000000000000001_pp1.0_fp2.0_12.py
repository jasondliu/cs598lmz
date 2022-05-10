import sys, threading

def run():
	#print(sys.argv)
	if len(sys.argv) < 2:
		print("Please provide a file to open")
		return

	fileName = sys.argv[1]
	file = open(fileName, "r")
	lines = file.readlines()
	file.close()

	#print(lines)
	#print(lines[0])
	#print(lines[0].split())

	input = lines[0].split()
	#print(input)
	#print(input[0])

	n = int(input[0])
	k = int(input[1])
	q = int(input[2])
	#print(n, k, q)

	input = lines[1].split()
	#print(input)
	a = [int(x) for x in input]
	#print(a)

	for i in range(k):
		a.insert(0, a.pop())

	for i in range(q):
		m = int(lines[i + 2])
	
