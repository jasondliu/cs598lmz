import select
# Test select.select([], [], [], 0)
print select.select([], [], [], 0)
print select.select([], [], [], 0.0)


import select
def test_read(stream):
	r,w,e = select.select([stream], [], [], 0)
	if r:
		return stream.read(1)
	return None

def test_write(stream, data):
	r,w,e = select.select([], [stream], [], 1)
	if w:
		return stream.write(data)
	return None

t = self.tcp_connect()
test_write(t, "hello")
# Test select.select([], [], [], 0)
print test_read(t)
print test_read(t)


import select
# Test select.select([], [], [], 0)
print select.select([], [], [], 0)
print select.select([], [], [], 0.0)


import select
# Test select.select([], [], [], 0)
print select
