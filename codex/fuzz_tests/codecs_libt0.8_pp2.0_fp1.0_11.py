import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def valid_credentials(username, password):
	"""Only a temporary validator."""
	USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
	def full_width_to_half_width(s):
		n = []
		for char in s:
			num = ord(char)
			if num == 0x3000:
				num = 32
			elif 0xFF01 <= num <= 0xFF5E:
				num -= 0xfee0
			num = chr(num)
			n.append(num)
		return ''.join(n)
	username = full_width_to_half_width(username)
	password = full_width_to_half_width(password)
	if USER_RE.match(username) and USER_RE.match(password
