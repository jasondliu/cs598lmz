import bz2
bz2.decompress(compressed)

# to read from file
with bz2.open('file.bz2', 'rt') as f:
    text = f.read()

# to write to file
with bz2.open('file.bz2', 'wt') as f:
    f.write(text)

# to read lines
with bz2.open('file.bz2', 'rt') as f:
    for line in f:
        print(line)

# compress multiple files
import bz2, glob
for filename in glob.glob('*.txt'):
    with open(filename, 'rb') as f_in, bz2.open(filename + '.bz2', 'wb') as f_out:
        f_out.write(f_in.read())

# decompress multiple files
import bz2, glob
for filename in glob.glob('*.bz2'):
    with bz2.open(filename, 'rb') as f_in, open(filename[:-4], 'wb') as f_out
