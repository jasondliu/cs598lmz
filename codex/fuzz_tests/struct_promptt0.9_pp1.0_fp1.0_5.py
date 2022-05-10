import _struct
# Test _struct.Struct.from_param()

from test.support import requires
from test.support.script_helper import assert_python_ok

def test_main():
    script = 'import _testbuffer\n'
    script += '_testbuffer.test_from_param()\n'
    assert_python_ok('-c', script)

@requires('_testcapimodule')
def test_from_param():
    from _testcapimodule import pymem_buffer

    b = bytearray(b'a\x00bc')
    buf = _struct.pack('i', 5)
    assert pymem_buffer(b, 10) == b'a\0bc\0\0\0\0\0\0'
    assert pymem_buffer(memoryview(b), 10) == 'a\0bc\0\0\0\0\0\0'
    # Py_buffer is not initialized, therefore pymem_buffer(buf, 5)
    # crashes Python interpreter
    #assert pymem_buffer(buf, 5) == b


