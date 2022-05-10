import bz2
bz2.decompress(open('/Users/ilya/Projects/dangerzone/data/train/0/0_0.bz2', 'rb').read())

# Set the path to the full NASA dataset file
full_dataset_path = '/Users/ilya/Projects/dangerzone/data/train/0/0_0.bz2'

with bz2.BZ2File(full_dataset_path) as f:
    for i, line in enumerate(f):
        print(line)
        if i == 2:
            break

# Read the first line of the file into a string
with bz2.BZ2File(full_dataset_path) as f:
    file_content = f.readline()

# Print the first 1000 characters of the file
print(file_content[:1000])

# Split the read bytes on newline characters
file_content_split = file_content.split(b'\n')

# Print the first 1000 characters of the first line
print(file_content_split[0][
