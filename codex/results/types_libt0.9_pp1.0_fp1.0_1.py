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

def read_token(s):
	global token_kind

	token_text = ''
	while True:
		c = s.read(1)
		if c == ' ':
			if len(token_text) > 0:
				break
			continue
		elif len(c) == 0:
			if len(token_text) > 0:
				break
			token_kind = 'EOF'
			break
		elif c
