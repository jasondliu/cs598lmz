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
view[0] = 1
</code>
How can I solve this?
EDIT:
I looked at pydevd.py and I am guessing that this is the code which calls <code>readinto</code> of the Python file:
<code> debugger_wrapper.run('while True:'
                          '    try:'
                          '        f = os.fdopen(%s)'%os.pipe()[0]+
                          '        break'
                          '    except:'
                          '        pass'
                          'buf = array.array("c",  "\\0"*%s)'%OUT_SIZE+
                          'while True:'
                          '    try:'
                          '        n = f.readinto(buf)'
                          '        if len(buf.tostring()) == 0:'
                          '            time.sleep(0.1)'
                          '            continue'
                          '    except IOError, ex:'
                          '        if ex.errno != errno.EWOULDBLOCK:'
                          '            raise'
                          '        continue'

