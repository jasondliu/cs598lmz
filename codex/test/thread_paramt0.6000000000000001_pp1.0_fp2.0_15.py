import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from onnx_coreml import convert
from coremltools.models import MLModel
from coremltools.models.neural_network import NeuralNetworkBuilder
from coremltools.models import datatypes
from coremltools.models.utils import save_spec
import coremltools
from coremltools.models.neural_network import flexible_shape_utils
from coremltools.proto import NeuralNetwork_pb2 as _NeuralNetwork_pb2
from coremltools.proto import FeatureTypes_pb2 as _FeatureTypes_pb2
from coremltools.models.utils import _macos_version
import numpy as np
import onnx
from onnx import numpy_helper
from onnx import helper, shape_inference
from onnx import helper, TensorProto, AttributeProto
import torch
from torch import nn
from torch.autograd import Variable
from torch.nn import functional as F
import torchvision
from torchvision import models
