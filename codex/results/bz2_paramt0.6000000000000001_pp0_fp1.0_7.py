from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda self: None

# Connect to the input stream
input = sys.stdin.buffer

# Create a BZ2 decompressor object
decompressor = BZ2Decompressor()

# Decompress the input stream
# and write the output to sys.stdout
while True:
    block = input.read(1024)
    if not block:
        break
    output = decompressor.decompress(block)
    if output:
        sys.stdout.buffer.write(output)
    if decompressor.unused_data:
        input = BytesIO(decompressor.unused_data)
        decompressor = BZ2Decompressor()

# Flush any remaining data
output = decompressor.flush()
if output:
    sys.stdout.buffer.write(output)

# Finish off and exit
sys.stdout.flush()
sys.exit(0)
