import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_void_p)

class CFileAssembler(object):
    def __init__(self, filename, constants_file, strings_file, all_func_fd, all_fun, arity_f, n_func_f):
        self.f = open(filename, 'w')
        self.cf = open(constants_file, 'w')
        self.sf = open(strings_file, 'w')
        self.all_func_fd = open(all_func_fd, 'w')
        self.all_fun = open(all_fun, 'w')
        self.arity_f = open(arity_f, 'w')
        self.n_func_f = open(n_func_f, 'w')
        self.in_function = False
        self.name_label = 0
        self.names_used = dict()
        self.function_names_labels = dict()
        self.function_names_locations = dict()
