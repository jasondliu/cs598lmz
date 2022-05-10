import ctypes
ctypes.cast(0, ctypes.py_object).value

#
# PyObject_AsReadBuffer(PyObject *obj, const void **buffer, Py_ssize_t *buffer_len)
#
# Return a pointer to a read-only memory buffer that contains the contents of obj.
#
# This must be a “readable” buffer object. The buffer’s contents will not be copied, so the original object must stay alive.
#
# If obj is not a readable buffer object, PyBuffer_FromObject() is called to create one.
#
# Return 0 on success, -1 on error.
#
# Changed in version 3.3: The obj argument can now be any object supporting the buffer protocol.
#
# New in version 3.0.
#

#
# PyObject_AsWriteBuffer(PyObject *obj, void **buffer, Py_ssize_t *buffer_len)
#
# Return a pointer to a writeable memory buffer into which obj’s contents can be copied.
#
# This must be a “writable” buffer object. The buffer’s contents will
