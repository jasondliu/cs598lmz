import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_uint)
def printf(format, *args):
    # the only way to print from .npy files is with this type of function
    func = FUNTYPE(('printf', ctypes.CDLL(None)))
    res = func(format % args)
    return res

# define a function here to be called by npy code.
def power_of_2(x):
    return 1<<x

if __name__ == '__main__':
    # Compile the numpy script given as the first argument
    # This will generate a support file in the output_dir
    # it will also return the name of the support file
    build_dir=os.path.abspath('build')
    output_dir=os.path.abspath('build')
    fname=os.path.abspath(sys.argv[1])
    ret = compile_to_support(fname, build_dir=build_dir, output_dir=output_dir, \
                             verbose=True, overwrite=True)
    #
