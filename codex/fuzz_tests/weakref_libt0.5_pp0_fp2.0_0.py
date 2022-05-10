import weakref

from .. import _backend
from .. import _utils
from .._utils import _set_input_dtype
from .._utils import _to_tuple
from .._utils import _to_list
from .._utils import _to_ndarray
from .._utils import _to_cuda_array_interface
from .._utils import _to_cuda_array_interface_compatible
from .._utils import _to_cuda_array_interface_compatible_ndarray
from .._utils import _get_device_id
from .._utils import _get_device
from .._utils import _get_device_from_array
from .._utils import _get_device_from_array_interface
from .._utils import _get_device_from_array_like
from .._utils import _get_device_id_from_array
from .._utils import _get_device_id_from_array_interface
from .._utils import _get_device_id_from_array_like
from .._utils import _get_device_from_id
from .._utils import _array_to
