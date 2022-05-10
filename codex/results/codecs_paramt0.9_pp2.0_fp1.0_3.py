import codecs
codecs.register_error('replace_with_space', codecs.replace_errors)
input_file = codecs.open('NOUNS_with_POS',encoding='utf-8',errors='replace_with_space')
output_file = codecs.open('NOUNS_with_POS_2',encoding='utf-8',errors='replace_with_space')
nr_lines = 0
for line in input_file:
	nr_lines += 1
	if line == None or line == '' or line == u'\n' or line==u'\ufeff':
		continue
	data = line.split(',')
	if len(data)!=2:
		print nr_lines
	output_file.write(data[0])
output_file.close()
input_file.close()
