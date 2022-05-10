import weakref

from vrms.analysis import analyse_package
from vrms.architecture import Architecture
from vrms.debian_utils import DebianVersion
from vrms.vendor import Vendor


class Package(object):
    """Object representing a Package.

    A package consists of a name, sections and a priority. As well as
    information about the package's use of non-free software.
    """

