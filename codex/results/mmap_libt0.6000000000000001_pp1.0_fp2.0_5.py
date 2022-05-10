import mmap
import os
import sys
import time
import traceback

from lib.cuckoo.common.config import Config
from lib.cuckoo.common.constants import CUCKOO_ROOT
from lib.cuckoo.common.exceptions import CuckooDisableModule
from lib.cuckoo.common.exceptions import CuckooDependencyError
from lib.cuckoo.common.exceptions import CuckooOperationalError
from lib.cuckoo.common.exceptions import CuckooProcessingError
from lib.cuckoo.common.exceptions import CuckooReportError
from lib.cuckoo.common.exceptions import CuckooResultError
from lib.cuckoo.common.exceptions import CuckooCriticalError
from lib.cuckoo.common.netlog import NetlogParser
from lib.cuckoo.common.objects import File
from lib.cuckoo.common.objects import URL
from lib.cuckoo.common.utils import create_folder
from lib.cuckoo.common.utils import delete_folder
from lib.cuckoo
