import codecs
codecs.getencoder(u'unicode_escape')

def encode(name):
	return codecs.encode(name, 'unicode_escape').replace(b'\\x',b'').decode('utf-8')

def generate_targets(targets):
	matches = []
	for target in targets:
		matches.extend(target)
	return matches

def gen_target_str(targets):
	return os.linesep.join(generate_targets(targets))

def gen_target_list(targets):
	return generate_targets(targets)

def format_bytes(b):
	if type(b) == str:
		return b
	return str(b, 'utf-8')

def parse_ip(a):
	if a.find(b'.') != -1:
		a = struct.unpack('I',socket.inet_aton(a))[0]
	return a

def restore_ip(a):
	return socket.
