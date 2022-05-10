import codecs
codecs.register_error('ignore', codecs.lookup_error('ignore'))

from .utils import FileWrapper
from .utils import get_path_from_pattern
from .utils import get_fs_from_pattern
from .utils import get_path_from_url
from .utils import get_fs_from_url
from .utils import get_pyarrow_filesystem
from .utils import get_pyarrow_filesystem_from_path
from .utils import get_pyarrow_filesystem_from_url
from .utils import get_filesystem_token
from .utils import get_filesystem_token_from_path
from .utils import get_filesystem_token_from_url
from .utils import get_filesystem_protocol
from .utils import get_filesystem_protocol_from_path
from .utils import get_filesystem_protocol_from_url
from .utils import get_fs_token_paths
from .utils import infer_compression
from .utils import infer_storage_options
from .utils import infer_compression_from_path
from .utils import infer_storage_options_
