import weakref

try:
    OrderedDict = collections.OrderedDict  # @UndefinedVariable
except AttributeError:
    # python < 2.7
    from fysom import OrderedDict

from pypet.naturalnaming.versioning import UndefinedVersion, VersionedHDF5StorageService

__author__ = 'Robert Meyer'

