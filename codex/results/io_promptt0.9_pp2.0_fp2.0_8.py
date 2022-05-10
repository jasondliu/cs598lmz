import io
# Test io.RawIOBase input
print(my_input)
# Test io.RawIOBase output
print(my_output.getvalue())

# Test write permissions using io.BytesIO
my_output = io.BytesIO()

with open('./data/bills.csv', 'rb') as f:
    my_input = io.BytesIO(f.read())

# Start a session that can be used for output
with Session(tempfiles.gettempdir()) as s:
    c1 = s.execute(
        my_input, 'hello_world', {
            'output': my_output,
            'output_write_permissions': 'wb'})
