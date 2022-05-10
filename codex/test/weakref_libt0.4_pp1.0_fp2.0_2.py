import weakref

from lib.cuckoo.common.abstracts import MachineManager
from lib.cuckoo.common.config import Config
from lib.cuckoo.common.constants import CUCKOO_ROOT
from lib.cuckoo.common.exceptions import CuckooMachineError
from lib.cuckoo.common.exceptions import CuckooCriticalError
from lib.cuckoo.common.exceptions import CuckooOperationalError
from lib.cuckoo.common.exceptions import CuckooResultError
from lib.cuckoo.common.objects import Dictionary
from lib.cuckoo.common.utils import create_folder
from lib.cuckoo.core.database import Database
from lib.cuckoo.core.database import TASK_COMPLETED
from lib.cuckoo.core.database import TASK_REPORTED
from lib.cuckoo.core.database import TASK_RUNNING
from lib.cuckoo.core.database import TASK_PENDING
from lib.cuckoo.core.database import TASK_FA
