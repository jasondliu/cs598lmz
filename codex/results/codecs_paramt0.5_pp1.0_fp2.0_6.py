import codecs
codecs.register_error('strict', codecs.ignore_errors)

def parse_args():
	parser = argparse.ArgumentParser(description='Convert a txt file to a UTF-8 file.')
	parser.add_argument('inputfile', metavar='INPUTFILE', help='the input file')
	parser.add_argument('outputfile', metavar='OUTPUTFILE', help='the output file')
	return parser.parse_args()

def main():
	args = parse_args()
	with open(args.inputfile, mode='r', encoding='utf-8') as infile:
		with open(args.outputfile, mode='w', encoding='utf-8') as outfile:
			for line in infile:
				outfile.write(line)

if __name__ == '__main__':
	main()
