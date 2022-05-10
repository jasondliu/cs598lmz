import select
# Test select.select()

# select() takes 3 lists:
#   1. The first is a list of the objects to be checked for being "ready" for reading
#   2. The second is a list of the objects to be checked for being "ready" for writing
#   3. The third is a list of the objects to be checked for errors.
#
# It returns a tuple containing three lists of objects that are "ready"
#   1. The first list contains the objects that are ready for reading
#   2. The second list contains the objects that are ready for writing
#   3. The third list contains the objects that have errors

# Create a list of sockets to be checked for reading
sockets_to_check_for_reading = []

# Create a list of sockets to be checked for writing
sockets_to_check_for_writing = []

# Create a list of sockets to be checked for errors
sockets_with_errors = []

# Create a list of sockets that are ready for reading
ready_to_read = []

# Create a list of sockets that are ready for writing
ready_to_write = []
