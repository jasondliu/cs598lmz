import _struct
from numpy.distutils.misc_util import get_numpy_include_dirs
from numpy.distutils.system_info import get_info, NotFoundError
from numpy.distutils.system_info import dict_append, dict_append_key
from numpy.distutils.system_info import BlasNotFoundError


# http://www.netlib.org/blas/blast-forum/cblas.tgz
# http://www.netlib.org/blas/blast-forum/cblas.tgz
# http://www.netlib.org/blas/blast-forum/cblas.tgz


def get_blas_info():
    def atlas_version(libpath):
        try:
            f = open(os.path.join(libpath, 'libatlas.a'), 'rb')
        except IOError:
            return None

        data = f.read(4096)
        f.close()

