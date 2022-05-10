fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
print(fn)
"""

# PyObject*
# PyCode_NewEmpty(const char *filename, const char *funcname, int firstlineno)
# {
#     PyObject *filename_ob = NULL;
#     PyObject *funcname_ob = NULL;
#     PyCodeObject *co = NULL;
#     if ((filename_ob = PyUnicode_DecodeFSDefault(filename)) == NULL)
#         goto fail;
#     if ((funcname_ob = PyUnicode_DecodeFSDefault(funcname)) == NULL)
#         goto fail;
#     co = (PyCodeObject *)PyCode_New(
#         0,            /*int argcount,*/
#         0,            /*int kwonlyargcount,*/
#         0,            /*int nlocals,*/
#         0,            /*int stacksize,*/
#         0,            /*int flags,*/
#         EMPTYBYTES,    /*PyObject *code,*/
#         EMPTYTUPLE,    /*PyObject *consts,*/
#
