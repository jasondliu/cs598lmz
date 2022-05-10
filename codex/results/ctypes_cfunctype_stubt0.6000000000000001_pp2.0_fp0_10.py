import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

with open("test.wasm", "rb") as f:
    raw = f.read()
s = str(base64.b64encode(raw))[2:-1]
print(s)

with open("test.wasm.base64", "w") as f:
    f.write(s)

with open("test.wasm.base64", "r") as f:
    s = f.read()
raw = base64.b64decode(s)

with open("test2.wasm", "wb") as f:
    f.write(raw)

with open("test.wat", "r") as f:
    info = f.read()
print(info)

with open("test.wat", "w") as f:
    f.write(info)

with open("test.wat", "r") as f:
    info = f.read()
print(info)

with open("test.json", "w") as f:
    f.write(info)

with open("test.
