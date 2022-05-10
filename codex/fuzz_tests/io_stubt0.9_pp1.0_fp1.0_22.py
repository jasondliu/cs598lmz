import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
del view
def bug():
    eval(u'\U0001f7cf'+u'()')
    eval(u'\U0001f7cf'.encode('utf-16')+u'()')
    eval(u'\U0001f7cf'.encode('latin-1')+u'()')

del bug
