import threading
threading.ENSURE_DETERMINISTIC = 1

import numpy as np

from mlshim import constant
from mlshim.utils import misc
from mlshim.utils.misc import make_spec_set
from ..managers.node_directory import NodeDirectory
from ..managers.parameters import ParameterManager


@pytest.fixture
def test_module_setup():
    """Initialize a mock module and a test directory."""
    np.random.seed(0)
    node_dir = NodeDirectory()
    module = DummyModule(node_dir, 'TestDummyModule')
    for node in module.nodes.values():
        node.register(node_dir)

    node_dir.get('weight').set_value(np.random.rand(10, 1))
    module.enable_gradient()
    return module


class TestDummyModule(object):
    def test_forward_with_gradient(self, module):
        outputs = module.forward()
        assert isinstance(outputs, torch.Tensor)
        expected_sum = torch.
