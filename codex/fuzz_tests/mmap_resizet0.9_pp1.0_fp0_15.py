import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = []
</code>
I've got <code>ValueError('mmap can't enlarge memory maps, mmap size is unchanged')</code> exception.
What is the problem?


A:

You could replace the file with a temporary file, with the desired size and the content from the mmap, and then rename the temp file, this will do the trick.
<code>import mmap
import contextlib
import os


def replace_file(file_path, new_file_in_string):
    """Replace the file with a new file."""
    with contextlib.ExitStack() as stack:
        # Create a temporary file.
        fd, temp_file_path = stack.enter_context(tempfile.mkstemp())

        # Fill the file with the new file.
        with os.fdopen(fd, 'w') as temp_file:
            temp_file.write(new_file_in_string)

        # Remove the original and rename the temp file.
        stack.callback(os.remove, temp_file_path)
        os.replace(temp_
