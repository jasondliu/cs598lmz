import threading
# Test threading daemon feature

def is_even_number(number):
	if number % 2 == 0:
		return True
	else:
		return False

class FindEvenNumber(threading.Thread):
	def __init__(self, number):
		threading.Thread.__init__(self)
		self.number = number

	def run(self):
		print("Find even number thread: {}".format(self.number))
		is_even_number(self.number)

def main():
	thread_list = []
	for i in range(1, 10):
		t = FindEvenNumber(i)
		# t.daemon = True # kill all the threads
		thread_list.append(t)
		t.start()
	for t in thread_list:
		t.join()
	print("Exiting Main Thread")

if __name__ == "__main__":
	main()
