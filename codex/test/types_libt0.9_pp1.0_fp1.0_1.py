import types
types.FrameType = FrameType

def parse_int(s):
	r = 0
	for c in s:
		r = r * 10 + ord(c) - ord('0')
	return r

def parse_float(s):
	r = 0.0
	k = 0
	for c in s:
		if c == '.':
			k = 1
			continue
		r = r * 10 + ord(c) - ord('0')
		k *= 10
	return r / k

