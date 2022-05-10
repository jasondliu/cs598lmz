import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

from . import __version__
from . import __description__
from .api import *
from .api import __all__ as api_all
from .core import *
from .core import __all__ as core_all
from .exceptions import *
from .exceptions import __all__ as exceptions_all
from .utils import *
from .utils import __all__ as utils_all
from . import io
from .io import __all__ as io_all
from . import models
from .models import __all__ as models_all
from . import stats
from .stats import __all__ as stats_all
from . import visualization
from .visualization import __all__ as visualization_all
from . import datasets
from .datasets import __all__ as datasets_all
from . import preprocessing
from .preprocessing import __all__ as preprocessing_all
from . import metrics
from .metrics import __all__ as metrics_all
from . import decomposition
