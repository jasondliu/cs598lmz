import bz2
# Test BZ2Decompressor on one of the sample files

# Copy the readme file to a local file
!cp ../input/jigsaw-toxic-comment-classification-challenge/sample_submission.csv.bz2 sample_submission.csv.bz2
# Open the compressed file
file = bz2.BZ2File('sample_submission.csv.bz2')
# Create a decompression object
decompressor = bz2.BZ2Decompressor()
# Read the compressed file data
file_data = file.read()
# Decompress the file data
uncompressed_data = decompressor.decompress(file_data)
# Write the extracted data to a local file
with open('sample_submission.csv', 'wb') as f:
    f.write(uncompressed_data)
# Now read the file data:
# Read the local file
sample_submission = pd.read_csv('sample_submission.csv')
# View the decompressed data
sample_submission.head()

print(sample_submission.shape)

# Now
