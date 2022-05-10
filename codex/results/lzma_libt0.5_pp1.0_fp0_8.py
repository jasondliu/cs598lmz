import lzma
lzma = lzma.LZMAFile(open('/home/pi/Desktop/Test/test.7z', 'rb'))

# Creating the file with the same name as the archive
lzma_decompressed = open('/home/pi/Desktop/Test/test.csv', 'wb')

# Decompressing the data
lzma_decompressed.write(lzma.read())

# Closing the files
lzma.close()
lzma_decompressed.close()

# Opening the file that was just created
csv_file = open('/home/pi/Desktop/Test/test.csv', 'r')

# Reading the file
csv_reader = csv.reader(csv_file)

# Creating a list of the values in the file
csv_data = list(csv_reader)

# Closing the file
csv_file.close()

# Creating a dictionary of the data
csv_dict = {rows[0]: rows[1] for rows in csv_data}

# Creating a list of the keys in the dictionary
csv_
