import threading
threading.stack_size(67108864) 

def execute_commands(commands):
	print("STARTING PARALLEL EXECUTION...")
	threads = []
	for command in commands:
		print("\t"+command)
		threads.append(threading.Thread(target=os.system, args=(command,)))
		threads[-1].start()
	for t in threads:
		t.join()
	print("END OF PARALLEL EXECUTION.")

def function01():
	#../../new_benchmarks/predictors/cnn.py ../../../datasets/open_images/hdf5/oivm_egocentric/ oivm_egocentric 0 1 testing same_split
	commands = []

	commands.append('python cnn.py ../../datasets/open_images/hdf5/oivm_egocentric/ oivm_egocentric 10 10 testing same_split ')
	#commands.append('python ./cnn.
