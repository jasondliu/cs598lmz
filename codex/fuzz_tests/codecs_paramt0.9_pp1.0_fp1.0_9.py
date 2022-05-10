import codecs
codecs.register_error('strict', codecs.ignore_errors) # compress, BOM error

def main():
	if len(sys.argv) != 3:
		print ('Usage: python3 {0} <first> <second>'.format(sys.argv[0]))
		sys.exit()
	mapfilename = sys.argv[1]
	ofilename = sys.argv[2]
	mfile = codecs.open(mapfilename, mode='r', encoding='utf-8', errors='strict')
	ofile = codecs.open(ofilename, mode='w', encoding='utf-8', errors='strict')
	
	# main processing
	line = mfile.readline()
	line = line.rstrip()
	line = line.strip()
	ofile.write('{0}\n'.format(line))
	line = mfile.readline()
	while line != '':
		line = line.rstrip()
		line = line.strip()
		fields = line.split(' ')
		if len(
