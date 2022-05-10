import bz2
bz2.BZ2File(filename).readlines()

# <codecell>

#Open a file for writing
f = open('workfile', 'w')

# <codecell>

# Get some stuff written
f.write('This is a test\n')

# <codecell>

# Close the file when done
f.close()

# <codecell>

# Open the file again
f = open('workfile', 'r')

# <codecell>

# Read the contents
f.read()

# <codecell>

# Readlines returns a list of strings, one string per line in the file
f.readlines()

# <codecell>

# Always close your files when done
f.close()

# <codecell>

# Open a file using a with statement. The file is properly closed after the suite finishes
with open('workfile') as f:
    read_data = f.read()

# <codecell>

f.closed

# <codecell>

f.read()

# <code
