import gc, weakref

from . import _utils

from ._utils import _get_default_session, _get_default_graph, _make_decorator

from ._utils import _default_graph_stack, _default_session_stack

from ._default_graph import _DefaultGraphStack, _DefaultGraphStackContext

from ._default_session import _DefaultSessionStack, _DefaultSessionStackContext

from ._utils import _get_graph_from_inputs

from ._utils import _get_graph_from_inputs, _get_graph_from_tensors

from ._utils import _get_session_from_inputs

from ._utils import _get_session_from_inputs, _get_session_from_tensors

from ._utils import _get_default_device

from ._utils import _get_default_device, _get_default_device_from_session

from ._utils import _get_default_device_from_graph

from ._utils import _get_default_device_from_graph, _get_default_device_from_session

from ._utils import _
