import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None) 

def read_file(filename):
	with open(filename, 'r') as f:
		return f.read()

def write_file(filename, content):
	with open(filename, 'w') as f:
		f.write(content)

#docx to utf8 txt
raw_txt = read_file('raw.txt').replace('\n', ' ')
raw_txt = raw_txt.replace('\r', ' ')
raw_txt = raw_txt.replace('\t', ' ')
raw_txt = raw_txt.replace('\f', ' ')
# raw_txt = raw_txt.replace(';', ' ')
raw_txt = raw_txt.replace(',', ' ')
raw_txt = raw_txt.replace('  ', ' ')
write_file('raw.txt', raw_txt)
