import codecs
codecs.register_error('strict', codecs.ignore_errors)

def split_log(filename, output_dir, max_lines=1000000):
	f = open(filename, 'r')
	lines = 0
	i = 0
	out_file = open(os.path.join(output_dir, "log-%d" % (i,)), 'w')
	for line in f:
		out_file.write(line)
		lines += 1
		if lines > max_lines:
			lines = 0
			i += 1
			out_file.close()
			out_file = open(os.path.join(output_dir, "log-%d" % (i,)), 'w')
	f.close()
	out_file.close()

def split_chatlog(filename, output_dir, max_lines=1000000):
	f = open(filename, 'r')
	lines = 0
	i = 0
	out_file = open(os.path.join(output_dir, "log-%d"
