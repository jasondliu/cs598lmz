from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

## 8. Reading a File in Binary Mode ##

# Open the file for reading in binary mode
with open("fivethirtyeight.csv", "rb") as file:
    # Read the whole file
    data = file.read()
    # Print the type of the file data
    print(type(data))

## 9. Binary Mode and Text Mode ##

# Read the whole file
with open("fivethirtyeight.csv", "r") as file:
    text_data = file.read()

# Print the first 500 characters
print(text_data[0:500])

# Read the whole file
with open("fivethirtyeight.csv", "rb") as file:
    binary_data = file.read()

# Print the first 500 characters
print(binary_data[0:500])

## 10. Reading Small Chunks of Binary Data ##

# Read the whole file
with open("fivethirtyeight.csv", "rb") as file:
    # Read the whole file at once
    data = file.read()

