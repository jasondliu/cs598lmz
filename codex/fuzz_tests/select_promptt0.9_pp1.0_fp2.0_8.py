import select
# Test select.select and select.poll each with an explicitly invalid non-timeout on a readable 
# file that is not readable:
#
# The file is opened as a readable and writable file.
#
# Testing shows that select.select and select.poll accept a value of -1 for the timeout (which 
# according to the docs is not acceptable) and return immediately with no file descriptors in 
# the selected set. A value of 0 (zero) is also acceptable and returns immediately with no file 
# descriptors in the selected set. 
#
# The documentation does not say what happens if an invalid value is given as the timeout for
# select.select and select.poll.
#
# In testing, select.select and select.poll both fail with a ValueError when an explicit integer 
# value is given that is not in the range 0 ... MAXINT.
#
# Both select.select and select.poll both fail with the exception of TypeError when the timeout 
# value is None.
#
# Both select.select and select.poll both fail with the exception of TypeError when the timeout 
# value is a floating point value. 
