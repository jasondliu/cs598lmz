import select
# Test select.select()

def check_keyboard():
	if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
		ch = sys.stdin.read(1)
		return ord(ch)
	return None

def test_select():
	for i in range(10):
		print i,
		sys.stdout.flush()
		ch = check_keyboard()
		if ch != None:
			print "Got character", ch
			break
		time.sleep(1)
	else:
		print "No keyboard activity detected"

if __name__ == '__main__':
	test_select()
