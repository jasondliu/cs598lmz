import _struct

from mpi4py import MPI

from spack.util.environment import *


def is_system_package(pkg):
    """True if the package is maintained by the system."""
    if pkg.external:
        return True

    if not pkg.installed:
        return False

    path = spack.store.layout.path_for_package(pkg)
    return '@spack' not in path


@memoized
def get_mpi_paths():
    spec = Spec('mpi')
    try:
        # load the MPI module and get paths to the MPI libraries/headers
        spec.concretize()
        module.load(spec)
        return (spec.prefix, spec.prefix.include, spec.prefix.lib)
    except Exception as e:
        tty.debug(e)
        tty.die("Unable to load MPI module to find MPI paths.")


@memoized
def get_compilers(mpi_spec):
    """Return a mapping of compiler names to tuples of:
      
