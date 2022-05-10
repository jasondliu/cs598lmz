import mmap
+# The module 'archive' has to be installed in Python first!
+import archive
+if __name__ == '__main__':
+	import optparse
+	op = optparse.OptionParser()
+	op.add_option('-v', '--verbose', dest='verbosity', action='count', default=0, help='Increase the verbosity level.')
+	op.add_option('-n', dest='num_blocks', default=9, type='int', help='Maximum number of blocks to read.')
+	op.add_option('-d', '--default', dest='default_answer', action='store_true', help='Use defaults if user does not set parameters.')
+	op.add_option('-f', '--file', dest='filename', type='string', help='File to convert.', default='test.stor')
+	options, args = op.parse_args()
+	with open(options.filename, 'rb') as f, archive.StorReader(f) as reader:
+		for i in range(options.num_
