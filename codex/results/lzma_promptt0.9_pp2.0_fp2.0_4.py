import lzma
# Test LZMADecompressor
with open('enwik9.xz', 'rb') as f:
    file_content = f.read()

file_content_decompressed = lzma.decompress(file_content)
 
# Print the first 200 characters of the decompressed data
print(file_content_decompressed[:200])

# Import pickle package
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head
