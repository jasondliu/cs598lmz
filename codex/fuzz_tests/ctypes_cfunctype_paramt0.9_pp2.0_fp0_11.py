import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)

#---
from .train import TrainPerceptronCL
from .train import TrainPerceptronGPU
from .predict import PredictPerceptronCL
from .predict import PredictPerceptronGPU

from .perceptron_gpu import GetPerceptronSize
from .perceptron_gpu import StripPerceptron
from .perceptron_gpu import FinalizePerceptron
from .perceptron_gpu import InitPerceptron
from .perceptron_gpu import AllocatePerceptron
from .perceptron_gpu import FreePerceptron
from .perceptron_gpu import SetPerceptronParams
from .perceptron_gpu import SetPerceptronTrainGPU
from .perceptron_gpu import SetPerceptronPredictGPU
from .perceptron_gpu import SetPerceptronTrainCL
from .perceptron_gpu import SetPerceptronPredictCL
from .perceptron_gpu import SetPerceptronCLFuncs
from .perceptron_gpu import
