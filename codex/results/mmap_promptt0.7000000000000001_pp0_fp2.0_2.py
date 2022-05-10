import mmap
# Test mmap.mmap()

#
# Open the file
#

f = open("/tmp/foo.txt", "r+b")
#
# Create the map
#
m = mmap.mmap(f.fileno(), 0)
#
# Print out the line that should be there
#
print m[:13]
#
# Close the file
#
f.close()
#
# Unmap the file
#
m.close()
</code>
The output is:
<code>Hello Python!
</code>

My question is, can I do a similar thing when I have a string instead of a file?  I tried the following:
<code>import mmap

str = "Hello Python!"

#
# Create the map
#
m = mmap.mmap(-1, len(str))

#
# Print out the line that should be there
#
print m[:13]

#
# Unmap the file
#
m.close()
</code>
But that throws an error:
<code>Traceback (most recent call last):

