import ctypes
ctypes.cast(0, ctypes.py_object).value

# PyObject_AsReadBuffer(PyObject *obj, const void **buffer, Py_ssize_t *buffer_len)
# PyObject_AsWriteBuffer(PyObject *obj, void **buffer, Py_ssize_t *buffer_len)

# Py_buffer
# PyObject_GetBuffer(PyObject *obj, Py_buffer *view, int flags)
# PyBuffer_FillInfo(Py_buffer *view, PyObject *obj, void *buf, Py_ssize_t len, int readonly, int flags)
# PyBuffer_Release(Py_buffer *view)

# PyObject_Format(PyObject *obj, PyObject *format_spec)
# PyObject_GetAttr(PyObject *obj, PyObject *name)
# PyObject_GetAttrString(PyObject *obj, const char *name)
# PyObject_HasAttr(PyObject *obj, PyObject *name)
# PyObject_HasAttrString(PyObject *obj, const char *name)
# PyObject_SetAttr
