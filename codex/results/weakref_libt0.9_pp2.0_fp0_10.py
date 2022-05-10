import weakref
import logging
import gc

logger = logging.getLogger(__name__)


def _create_mock_node(node, name="node"):
    """ This mock gains all desired properties.
    """
    if not hasattr(node, "key"):
        setattr(node, "key", mock.Mock(return_value=node))

    return mock.MagicMock(name=name, spec=node, wraps=node)


def enumerate_mock_node(node, **kwargs):
    """ This method will enumerate a mock object model like a node.
    """
    return _enumerate(node=node, mock=True, **kwargs)


def enumerate_persisting_node(node, session=None, **kwargs):
    """ This method will enumerate a real object model like a node.
    """
    return _enumerate(node=node, session=session, mock=False, **kwargs)


def _enumerate(node, session=None, mock=False, selected=None,
               hidden=None
