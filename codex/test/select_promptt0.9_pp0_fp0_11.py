import select
# Test select.select()
# Select on input (0), output (1), or exception (2)/
def test_Select():
	# Make a tty and redirect it as stdin
	tty = os.open('/dev/tty', os.O_RDWR)
	old_stdin = os.dup(0)
	os.dup2(tty, 0)

	# Wait for stdin to become readable.
	# This does not work with stdin of a python program.
	reads, writes, excepts = select.select([sys.stdin], [], [], 60)

	if reads:
		# Resume stdin.
		os.dup2(old_stdin, 0)
		os.close(old_stdin)
		os.close(tty)

		# Read in a line and do something with it
		line = sys.stdin.readline().rstrip()
		print('You typed:', line)
	else:
		print('Timed out')


# Test select select()
test_Select()

#! /usr
