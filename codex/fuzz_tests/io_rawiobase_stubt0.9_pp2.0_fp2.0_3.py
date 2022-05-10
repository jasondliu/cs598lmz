import io
class File(io.RawIOBase): def __init__(self, _): pass


def generator():
	assert isinstance(sys.stdin.buffer, File)
	for line in sys.stdin:
		n = int(line)
		if n == 0:
			raise StopIteration
		yield n

lengths = generator()
while lengths:
	print('The maximum winning streak is {}.'.format(get_max_winning(lengths)))
	try: next(lengths)
	except StopIteration: lengths = None
