import select
# Test select.select()

# List of socket descriptors we want to wait for reading:
inputs = [ ]

# List of socket descriptors we want to wait for writing:
outputs = [ ]

# List of socket descriptors we want to wait for _exceptional_ conditions:
exceptional = [ ]

