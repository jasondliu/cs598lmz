import codecs
codecs.register_error('strict', codecs.replace_errors)

def main():
	fout=codecs.open('output-question.txt', 'a', encoding='utf8')
	for fname in glob.glob('output/question/book/*.txt'):
		with codecs.open(fname, 'r', encoding='utf-8', errors='strict') as f:
			for line in f:
				if(line[0:4]=='<DOC'):
					start_str='<DOCNUM> '
					start_pos=line.find(start_str)+len(start_str)
					end_pos=line.find('<', start_pos)
					docno=line[start_pos:end_pos]
				elif(line[0:6]=='<TEXT>'):
					text=' '
					while True:
						line=f.next()
						
