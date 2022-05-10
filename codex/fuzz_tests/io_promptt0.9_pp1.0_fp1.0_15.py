import io
# Test io.RawIOBase.read function
fp = io.BytesIO()
fp.write(b'hoge')
fp.seek(0)
fp.read(2) # first time
fp.read(2) # second time
fp.read(2) # third time
f = open('README.rst')
f.read(1)
f.write(b' ')
f.read(1)
import io
bio = io.BytesIO()
bio.write(b'this is test')
bio.read(3)
bio.write(b'')
import io
bio = io.BytesIO()
bio.write(b'hogehoge')
bio.seek(0)
bio.read1(4) # first time
bio.read1(4) # second time
bio.read1(4) # third time
import io
fp = io.BytesIO()
fp.write(b'hoge')
fp.seek(0)
fp.read1(2) # first time
fp.read1(2) # second time
fp.
