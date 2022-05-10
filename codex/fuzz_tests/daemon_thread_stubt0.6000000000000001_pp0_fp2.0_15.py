import sys, threading

def run():
	while True:
		try:
			# Get input
			_input = sys.stdin.readline()

			# Remove newline
			_input = _input.replace("\n", "")

			# Split input
			_input = _input.split(" ")

			# Check if user wants to quit
			if _input[0] == "quit":
				sys.exit()

			# Check for invalid input
			if len(_input) != 2:
				print("Invalid input")
				continue

			# Check if user wants to list files
			if _input[0] == "list":
				# Get list of files and print
				_files = os.listdir(_input[1])
				for _file in _files:
					print(_file)

			# Check if user wants to remove a file
			if _input[0] == "remove":
		
