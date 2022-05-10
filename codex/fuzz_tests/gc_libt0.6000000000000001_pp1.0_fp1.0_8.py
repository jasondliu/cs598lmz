import gc, weakref

from ..utils import print_msg, print_error
from .. import bitcoin
from ..transaction import Transaction
from ..bitcoin import COIN
from ..i18n import _
from ..util import profiler, bfh, bh2u, timestamp_to_datetime

if TYPE_CHECKING:
    from .main_window import ElectrumWindow


class Abstract_Wallet(PrintError):
    """
    Wallet classes are created to handle various address generation methods.
    Completion states (watching-only, single account, no seed, etc) are handled inside classes.
    """

    max_change_outputs = 3

    def __init__(self, storage):
        self.electrum_window = None  # type: 'ElectrumWindow'
        self.storage = storage
        self.network = None
        self.gap_limit_for_change = 6 # constant
        # saved fields
        self.seed_version          = storage.get('seed_version', NEW_SEED_VERSION)
        self.use_change            = storage.get('use_change', True)
        self.
