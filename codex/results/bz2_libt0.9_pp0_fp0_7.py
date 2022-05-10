import bz2
bz2_file=bz2.BZ2File('data.csv.bz2')
data=csv.reader(bz2_file)

for line in data:
    print (line)

# reading whole file into memory
bz2_file=bz2.BZ2File('data.csv.bz2')
whole_file_data=bz2_file.read()
bz2_file.close()
print (whole_file_data)


# Writing to a file - ZIP File
import zipfile

with zipfile.ZipFile('names.csv.zip', 'w') as zip:
    zip.write('data.csv',compress_type=zipfile.ZIP_DEFLATED)


# Writing to a file - bz2 file
import bz2
bz2_file=bz2.BZ2File('names.csv.bz2','w')
bz2_file.write(b'hello world')
bz2_file.close()

#Writing to a file - gz file
import gzip

