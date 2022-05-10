import _struct

# Name of the file.
file_name = "Demo.dat"

# Create the file.
file_handle = open(file_name, "wb")

# Add some data.
data = [1, 2, 3, 4, 5]
file_handle.write(_struct.pack(">5i", *data))

# Close the file.
file_handle.close()
