import select
# Test select.select.

# Add a character to a buffer.
def add (buf, char):
    # Get buffer as a list.
    buffer = list (buf)
    # Remove last element (oldest).
    buffer.pop()
    # Insert new character.
    buffer.insert(0, char)
    # Make buffer a string.
    return ''.join (buffer)

# Create stdin buffers.
inbuf = ""

# Create stdout buffers.
outbuf = "                        "

# Create stderr buffers.
errbuf = "                        "

# Create the selection list.
while True:
    # Use select.
    i, o, e = select.select ( [sys.stdin], [sys.stdout], [sys.stderr], 0)
    if i:
        # Read any incoming character.
        char = sys.stdin.read(1)
        # Add the character to the input buffer.
        inbuf = add (inbuf, char)
        # Print the buffer.
        sys.stdout.write (inbuf)
