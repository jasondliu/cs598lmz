import io
# Test io.RawIOBase class

# io.RawIOBase.read()
with io.BytesIO(bytes(10)) as f:
    try:
        f.read()
    except Exception as e:
        print(type(e))

# io.RawIOBase.readall()
with io.BytesIO(bytes(10)) as f:
    try:
        f.readall()
    except Exception as e:
        print(type(e))

# io.RawIOBase.readinto()
with io.BytesIO(bytes(10)) as f:
    try:
        f.readinto()
    except Exception as e:
        print(type(e))

# io.RawIOBase.readinto1()
with io.BytesIO(bytes(10)) as f:
    try:
        f.readinto1()
    except Exception as e:
        print(type(e))

# io.RawIOBase.readline()
with io.BytesIO(bytes(10)) as f:
    try:
        f.readline()
    except Exception as e:
       
