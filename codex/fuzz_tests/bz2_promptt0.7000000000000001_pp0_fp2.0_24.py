import bz2
# Test BZ2Decompressor class

decomp = bz2.BZ2Decompressor()

input_file = bz2.BZ2File('enwiki-latest-pages-articles1.xml-p10p30302.bz2', 'rb')
output_file = open('outfile.xml', 'w')

try:
    while True:
        block = input_file.read(100000)
        if not block:
            break
        output_file.write(decomp.decompress(block))
finally:
    input_file.close()
    output_file.close()
 
# skip the header line, which starts with "<!DOCTYPE mediawiki"

with open('outfile.xml', 'r') as infile:
    for line in infile:
        if line.startswith('<!DOCTYPE mediawiki'):
            continue
        else:
            print(line)
        
        break

# now process the data!

with open('outfile.xml', 'r') as infile:
    for line in infile:
