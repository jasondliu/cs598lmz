import bz2
bz2_file = bz2.BZ2File('/Users/alfonsodamelio/Desktop/Python/Python-for-informatics/Week9/output.bz2', 'wb')
bz2_file.write(original_data)
bz2_file.close()

# Reading a BZ2 compressed file
bz2_file = bz2.BZ2File('/Users/alfonsodamelio/Desktop/Python/Python-for-informatics/Week9/output.bz2', 'rb')
data = bz2_file.read()
bz2_file.close()
data

# Compressing data with gzip
import gzip
s = 'We are delighted to welcome you to the Foothills of the Piedmont'
out = gzip.open('/Users/alfonsodamelio/Desktop/Python/Python-for-informatics/Week9/output.gz', 'wb')
out.write(s)
out.close()

# Reading a gzip compressed file
gzip.open('/Users/alfonsodamel
