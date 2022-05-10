fn = lambda: None
# Test fn.__code__ attributes
print(fn.__code__.co_filename)
print(fn.__code__.co_name)
print(fn.__code__.co_firstlineno)
print(fn.__code__.co_flags)

# Read fn.__code__.co_filename to get the file's name.
fn_name = fn.__code__.co_filename.split('/')[-1].split('.')[0]
# Then use linecache.getline to extract the line.
source_code_line = linecache.getline(fn.__code__.co_filename, fn.__code__.co_firstlineno)

# Check if the function is actually a lambda function
is_lambda = fn.__code__.co_flags & 0x20

print(fn_name)
print(source_code_line)
print(is_lambda)

# Print the line.
print(fn_name + ': ' + source_code_line)


""" all of which can be condensed to: """

from functools import partial

print =
