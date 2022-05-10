fn = lambda: None
# Test fn.__code__.co_filename
print(fn.__code__.co_filename)

# Create a function to get the code object and filename
def get_code_filename(fn):
    return fn.__code__.co_filename
# Get function filename
print(get_code_filename(fn))

# Create a regular expression to match a filename
regexp = re.compile('(.+)\.py')
def get_code_filename2(fn):
    if regexp.match(path.basename(fn.__code__.co_filename)):
        # Get the filename and return it
        return path.basename(fn.__code__.co_filename)
    else:
        raise ValueError("Filename does not end with .py")

# Test for valid filename
print(get_code_filename2(fn))

# Test for invalid filename
fn.__code__.co_filename = "xyz"
try:
    get_code_filename2(fn)
except ValueError as e:
    print(e)

# Define a function within another function
def
