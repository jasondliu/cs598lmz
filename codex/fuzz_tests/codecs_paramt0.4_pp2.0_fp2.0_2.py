import codecs
codecs.register_error('strict', codecs.ignore_errors)

from . import config
from . import util
from . import errors
from . import log
from . import version

from .util import get_info, get_repo_info, get_repo_version
from .util import get_repo_root, get_repo_url, get_repo_name
from .util import get_repo_root_url, get_repo_root_name
from .util import get_repo_root_version, get_repo_root_info
from .util import get_repo_root_version_info, get_repo_root_url_info
from .util import get_repo_root_name_info, get_repo_root_info_info
from .util import get_repo_root_version_info_info
from .util import get_repo_root_url_info_info
from .util import get_repo_root_name_info_info
from .util import get_repo_root_info_info_info
from .util import get_
