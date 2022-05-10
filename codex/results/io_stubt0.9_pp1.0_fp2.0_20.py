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
print len(view)
print view
del view
''')
    print len(res.strip())
    assert res.strip() == '0'

    res = run('''
#include <Python.h>
#include <iostream>

int main(int argc, char **argv) {
    Py_Initialize();

    PyRun_SimpleString(
        "import io;"
        "with io.BytesIO(b'a') as f:"
        "   print hasattr(f, '__exit__');"
        "   f.write(b'a');"
        "   view = f.getbuffer();"
        "   print(len(view));"
        "   print(view);"
    );
    return 0;
}
''')
    assert res.splitlines() == [
        "True",
        "1",
        "b'aa'",
    ]

    res = run('''
#include <Python.h>
#include <iostream>

int main(int argc, char **argv) {
