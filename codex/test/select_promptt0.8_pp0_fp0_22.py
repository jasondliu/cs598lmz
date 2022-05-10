import select
# Test select.select()
# select() will block until an item in the list of all file descriptors
# has something to report
# Note: select() doesn't work on Linux and will block
#       indefinitely on an empty list of file descriptors
