import ctypes
ctypes.cast(0, ctypes.py_object).value

# 如果你想在一个 C 函数中改变 Python 对象的值，你需要使用指针。比如，下面是一个简单的 C 函数，它接受一个 Python 列表对象并修改它的值：
# example.c
#
#     #include <Python.h>
#
#     static PyObject *
#     extend_list(PyObject *self, PyObject *args)
#     {
#         PyObject *list;
#         PyObject *value;
#
#         if (!PyArg_ParseTuple(args, "OO", &list, &value))
#             return NULL;
#
#         if (PyList_Check(list)) {
#             PyList
