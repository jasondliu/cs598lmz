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

    def __init__(self, name, version, architecture=Architecture.ALL,
                 priority=Priority.UNKNOWN, vendor=Vendor.UNKNOWN,
                 sections=None, status=None, size=0, maintainer=None,
                 description=None, md5sum=None, target=None,
                 recommends=None, suggests=None, pre_depends=None,
                 depends=None, replaces=None, conflicts=None,
                 enhances=None, provides=None, source=None,
                 installed=False, is_source=False,
                 architecture_all=False, architecture_any=False,
                 architecture_none=False, architecture_specific=False,
                
