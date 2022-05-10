import io
# Test io.RawIOBase
!cat /Users/peadarcoyle/repos/learn-python-3-hard-way/exercises/ex_16_reading_and_writing_files/test.txt

f = open('/Users/peadarcoyle/repos/learn-python-3-hard-way/exercises/ex_16_reading_and_writing_files/test.txt', 'rb')
reader = io.BufferedReader(f)
print(reader.read())

print(reader.read())

print(reader.read())

f.close()



# Test io.BufferedIOBase
f = open('/Users/peadarcoyle/repos/learn-python-3-hard-way/exercises/ex_16_reading_and_writing_files/test.txt', 'r')
reader = io.BufferedReader(f)
print(reader.read(8))

print(reader.read(8))

print(reader.read(8))

f.close()

# Test io.TextIOBase
f = open('/Users
