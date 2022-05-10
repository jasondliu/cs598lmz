import ctypes
ctypes.cdll.LoadLibrary('caffe2_nvrtc.dll')

# This is needed to prevent errors caused by too many open
# files on the windows platform
if platform.system() == 'Windows':
    import win32api
    win32api.SetHandleInformation(0, win32con.HANDLE_FLAG_INHERIT, 0)

from caffe2.caffe2_pybind11_state import Caffe2State
from caffe2.python import core, workspace


def _set_random_seed(random_seed):
    """Sets the random seed in a deterministic way for reproducibility."""
    if random_seed is None:
        random_seed = 0
    if random_seed == -1:
        random_seed = None
    if random_seed is not None:
        np.random.seed(random_seed)
        random.seed(random_seed)


def _get_caffe2_op_set():
    return core.GetRegisteredOperators()


def create_model_helper():
    return Caffe2ModelHelper()


def
