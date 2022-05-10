import codecs
codecs.register_error('blank_error', codecs.replace_errors(u'\uFFFD'))

def find_key(name, group):
	return group._meta.get_field(name)

def validate_value(key, value):
	return key.data_type(value)

def convert_dict(d):
	return {convert_key(k): convert_value(v) for (k, v) in d.items()}

def convert_string(s):
	return s.encode('utf-8')

def convert_key(k):
	if isinstance(k, str) or isinstance(k, unicode):
		return convert_string(k)
	return k

def convert_value(v):
	if isinstance(v, str) or isinstance(v, unicode):
		return convert_string(v)
	if isinstance(v, dict):
		return convert_dict(v)
	return v


class TestHJson(unittest.TestCase):
	def setUp(self):
		self
