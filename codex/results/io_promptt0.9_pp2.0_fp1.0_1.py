import io
# Test io.RawIOBase output.

expected = "Te st."
with open(os.devnull, "wb") as f:
    w = io.BufferedWriter(io.RawIOBase(), buffer_size=8)
    w.write(expected.encode("utf-8"))
    w.flush()
    data = b""
    while True:
        try:
            chunk = f.read(8)
        except BlockingIOError:
            continue
        else:
            if chunk == b"":
                break
            data += chunk

assert data == expected.encode("utf-8")
