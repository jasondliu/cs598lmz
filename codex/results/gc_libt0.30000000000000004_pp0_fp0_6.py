import gc, weakref

from . import _util
from ._util import _get_default_session, _get_default_graph
from ._util import _make_numpy_array, _default_graph_stack, _default_session_stack
from ._util import _as_tf_output, _as_tf_output_list, _as_tf_shape, _as_shape, _shape_tuple
from ._util import _default_context_selector, _set_default_context_selector, _get_default_context
from ._util import _default_device_function_stack, _default_device_stack, _default_colocation_stack
from ._util import _default_control_flow_context_stack, _default_colocate_stack
from ._util import _default_control_dependencies_stack, _default_name_scope_stack
from ._util import _default_variable_creator_stack, _default_variable_scope_stack
from ._util import _default_name_stack, _default_graph_key_stack, _default_graph_stack, _default_graph_uid_stack
from ._util import
