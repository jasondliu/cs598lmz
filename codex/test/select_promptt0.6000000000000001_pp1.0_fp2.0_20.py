import select
# Test select.select()

# A function to simulate a blocked read.
def blocked_read():
    """ Simulate a blocked read. """
    # Sleep for 1 second.
    time.sleep(1)
    # Return some data.
    return "Blocked read return value."

# A function to simulate a blocked write.
def blocked_write():
    """ Simulate a blocked write. """
    # Sleep for 1 second.
    time.sleep(1)
    # Return a value.
    return "Blocked write return value."

# Return values from the functions.
read_return_value = None
write_return_value = None

# Define a list of readers and writers.
readers = [ blocked_read ]
writers = [ blocked_write ]

# Check for data to read or write.
