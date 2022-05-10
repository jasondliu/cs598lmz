import codecs
codecs.register_error('ig', codecs.ignore_errors)

postings = None
for filename in os.listdir('clusters'):
	if re.match('\d+\.html', filename):
		print 'reading', filename
		try:
			with codecs.open(os.path.join('clusters', filename), encoding='utf-8', errors='ig') as f:
				html = f.read()
		except :
			continue
		if not html:
			print 'empty file', filename
			continue
		if not postings:
			postings = html
		else:
			postings += '\n' + html

with codecs.open('all-postings.html', 'w', encoding='utf-8') as f:
	f.write(postings)

print 'done'
