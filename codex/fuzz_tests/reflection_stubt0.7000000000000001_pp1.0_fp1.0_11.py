fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

m1 = memoryview(b'a')
m1.__doc__ = gi

m2 = memoryview(b'a')
m2.__length_hint__ = gi

m3 = memoryview(b'a')
m3.__reduce__ = gi

m4 = memoryview(b'a')
m4.__reduce_ex__ = gi


def add_docstring(module):
    p = os.path.join(module.__path__[0], 'memoryview_doc.i')
    doc = open(p, 'rb').read()
    doc = doc.replace(b'_Py_TYPE(&PyByteArrayIter_Type)',
                      b'&PyByteArrayIter_Type')
    doc = doc.replace(b'_Py_TYPE(&PyMemoryView_Type)',
                      b'&PyMemoryView_Type')
    module.__doc__ += doc.decode("ascii")


add_docstring(memoryview)
