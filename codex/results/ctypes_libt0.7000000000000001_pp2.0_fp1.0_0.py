import ctypes
ctypes.cdll.LoadLibrary('libgfortran.so')
ctypes.cdll.LoadLibrary('libquadmath.so')

from numpy.distutils.fcompiler import FCompiler
from distutils.errors import DistutilsExecError

compilers = ['PathScaleFCompiler']

class PathScaleFCompiler(FCompiler):

    compiler_type = 'pathscale'
    description = 'PathScale Fortran Compiler'
    version_pattern = r'PathScale\s*Compiler\s*Version\s*(?P<version>[^\s]*)'
    version_match = True

    executables = {
        'version_cmd'  : ["pathf95", "--version"],
        'compiler_f77' : ["pathf95"],
        'compiler_fix' : ["pathf95"],
        'compiler_f90' : ["pathf95"],
        'linker_so'    : ["pathf95", "-shared"],
        'archiver'     : ["ar", "-cr"],
        'ranlib'       : ["ranlib
