import bz2
bz2.BZ2File(filename).read()

# This time, instead of using the 'with' keyword, we use the 'try' keyword to
# explicitly catch errors.
try:
    with open(filename, 'rt') as infile:
        print(infile.read())
except FileNotFoundError as ex:
    print(ex)
except Exception as ex:
    print(ex)

# Let's create a file for writing.
with open(filename, 'wt') as outfile:
    outfile.write("This is a test.\n")

# And let's open it in append mode.
with open(filename, 'at') as outfile:
    outfile.write("This is a test.\n")

# We can also create a file by reading from another file.
with open(filename, 'rt') as infile:
    with open("newfile.txt", 'wt') as outfile:
        for line in infile:
            outfile.write(line)

# We can also read a file in chunks.
with open(filename, 'rb') as
