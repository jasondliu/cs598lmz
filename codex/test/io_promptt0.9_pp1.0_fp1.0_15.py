import io
# Test io.RawIOBase.read function
fp = io.BytesIO()
fp.write(b'hoge')
fp.seek(0)
fp.read(2) # first time
fp.read(2) # second time
fp.read(2) # third time
