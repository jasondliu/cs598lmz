from bz2 import BZ2Decompressor
BZ2Decompressor.decompress

#os.system('/home/matt/Dropbox/Baylor/Research/Spring16/scripts/reformat_fastq.sh ' + filename)

new_filename = filename.split('.')[0] + '.fastq'

with open(new_filename) as f:
	for line in f:
		header = line.strip()
		seq = f.next().strip()
		f.next()
		qual = f.next().strip()
		print header
		print seq
		print qual
