import weakref
from tensorbach.models.nn.layers import Linear
from tensorbach.models.nn.initializers import HeInitializer, ZerosInitializer
from utils import test_auc, test_f1, count_parameters


def test_init_params():
    linear = Linear(input_size=5, output_size=1)

    zero_linear = Linear(input_size=5, output_size=1, weight_initializer=ZerosInitializer())
    zero_linear._init_parameters()
    assert linear.W.data.sum() != 0
    assert zero_linear.W.data.sum() == 0

    he_linear = Linear(input_size=5, output_size=1, weight_initializer=HeInitializer())
    he_linear._init_parameters()
    assert linear.W.data.sum() != he_linear.W.data.sum()


def test_linear_layer():
    linear = Linear(5)

    test_point_1 = torch.rand(4, 5)
    test_point_2 = torch.rand
