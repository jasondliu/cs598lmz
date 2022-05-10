import bz2
bz2_file = bz2.BZ2File(file_path + r"/mtcars.txt.bz2")
data = []
for line in bz2_file:
    data.append(line.decode("utf-8"))
    
# Open the class grades file for reading and read it into memory.
with gzip.open(file_path + r"/classgrades.txt.gz", "rb") as classfile:
    grades_list = classfile.readlines()
    
# After reading the file, decode each line and add the grade data to a dictionary
grades = {}
for grade in grades_list:
    (key, val) = grade.decode("utf-8").split(",")
    grades[key] = int(val)

# After reading in the cars data and the grades data, we can close the files
bz2_file.close()
classfile.close()

# Now, work with the data in memory.

# Print the header line of the cars data.
print(data[0])

# Use a for loop to extract the miles-
