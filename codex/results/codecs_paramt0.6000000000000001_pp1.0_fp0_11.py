import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_file(filename):
	f = codecs.open(filename, 'r', 'utf-8', 'replace_with_space')
	#f = codecs.open(filename, 'r', 'utf-8')
	data = f.read()
	f.close()
	return data

def write_file(filename, data):
	f = codecs.open(filename, 'w', 'utf-8')
	f.write(data)
	f.close()

def read_file_lines(filename):
	f = codecs.open(filename, 'r', 'utf-8')
	data = f.readlines()
	f.close()
	return data

def get_list_from_file(filename):
	data = read_file(filename)
	return data.strip().split('\n')

def get_list_from_file_strip(filename):
	data = read_file(filename)
	return [x.strip() for x in data.strip
