import codecs
codecs.register_error('replace_with_space', 
	lambda exc: (u' ', exc.start + 1))

def read_file(input_file, delimiter):
	with codecs.open(input_file, 'r', 'utf-8', 'replace_with_space') as f:
		lines = [line.strip().split(delimiter) for line in f]
	return lines

def read_data(input_file, delimiter):
	lines = read_file(input_file, delimiter)
	
	return lines

def write_data(output_file, delimiter, data):
	with codecs.open(output_file, 'w', 'utf-8') as f:
		for line in data:
			f.write(delimiter.join(line) + '\n')

def main():
	args = sys.argv[1:]

	if len(args) != 2:
		print 'usage: python split_text.py <input> <output>'
		sys.exit(1)

	input_file =
