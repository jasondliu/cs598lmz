import mmap
# Test mmap.mmap
"""
a = mmap.mmap(-1, 100)
a[0:10] = '0123456789'
a.close()
"""


# Check whether the file is empty
def is_empty(file_name):
    return os.stat(file_name).st_size == 0


# Delete the file
def del_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


# Create a file
def create_file(file_name):
    del_file(file_name)
    f = open(file_name, 'w')
    f.close()


# Write to the file
def write_file(file_name, content):
    f = open(file_name, 'w')
    f.write(content)
    f.close()


# Read the file
def read_file(file_name):
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return content


# Copy file
