import io
# Test io.RawIOBase's syntactic sugar for the *IO() functions
buf = io.BytesIO()
buf.write("hello world\n")
buf.seek(6)
buf.write("there\n")
print buf.read()
print buf.readline()

print("---")

buf = io.BytesIO()
buf.write("hi world\n")
buf.seek(0)
print buf.readline()
print buf.readline()

print("---")

buf = io.BytesIO("short\nbu\ht")
print buf.readline(10)
print buf.readline(10)

print("---")

buf = io.BytesIO("short\nbu\ht")
for chunk in iter(lambda: buf.read(3), ''):
    print chunk

buf = io.BytesIO("short\nbu\ht")
print list(iter(lambda: buf.read(3), ''))

print("---")

buf = io.BytesIO("short\nbu\ht")
print buf.readlines()
buf = io.BytesIO("short
