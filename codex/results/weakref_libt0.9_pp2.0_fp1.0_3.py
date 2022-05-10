import weakref

try:
    OrderedDict = collections.OrderedDict  # @UndefinedVariable
except AttributeError:
    # python < 2.7
    from fysom import OrderedDict

from pypet.naturalnaming.versioning import UndefinedVersion, VersionedHDF5StorageService

__author__ = 'Robert Meyer'

class MultiCapturePersistor(object):
    """Persistor for `Trajectory` that mimics the `TrajectoryHDF5StorageService`.

    Can be used with the `Trajectory` to capture results that are produced
    during a simulation and store those on disk. Takes care of naming the
    results in the same `Trajectory` storage hierarchy, making sure that
    all storage services work with the same storage hierarchy.

    The essential difference to the `TrajectoryHDF5StorageService` is that
    you do not need to create a separate storage service for every root
    node of a trajectory, but you can store data in only one hdf5 file
    (as long as the hierarchy does not exceed the maximum number of groups for a hdf5
