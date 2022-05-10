import bz2
bz2.BZ2File(fname, 'r')

# Read the file
file_content = bz2_file.read()

# Decode the content
file_content_decoded = file_content.decode('utf-8')

# Print the file
print(file_content_decoded)

# Close the file
bz2_file.close()

# Read & print the first 3 lines
with bz2.BZ2File(fname) as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

# Import pandas
import pandas as pd

# Import the bz2 file, and store the results
data = pd.read_csv(fname, sep='\t', compression='bz2')

# Plot the size of each category
data.groupby('Category')['Size'].mean().plot(kind='bar')
plt.show()

# Import pickle package
import pickle

# Open pickle file and load data: d
with open('
