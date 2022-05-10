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
