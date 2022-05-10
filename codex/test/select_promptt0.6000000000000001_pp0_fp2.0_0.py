import select
# Test select.select()

def check_keyboard():
	if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
		ch = sys.stdin.read(1)
		return ord(ch)
	return None

