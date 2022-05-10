import io
# Test io.RawIOBase class to check if a string can be read from it
test_raw_io = io.RawIOBase()
print(isinstance(test_raw_io, io.RawIOBase))
# Test io.BufferedIOBase class to check if a string can be read from it
test_buffer_io = io.BufferedIOBase()
print(isinstance(test_buffer_io, io.BufferedIOBase))
# Test io.TextIOBase class to check if a string can be read from it
test_text_io = io.TextIOBase()
print(isinstance(test_text_io, io.TextIOBase))

# Test io.FileIO class to check if a file can be read from it
file_path = "../data/raw/SMSSpamCollection"
test_file_io = io.FileIO(file_path)
print(isinstance(test_file_io, io.FileIO))

# Test io.StringIO class to check if a string can be read from it
test_string_io = io.StringIO()
print(isinstance(test_string_
