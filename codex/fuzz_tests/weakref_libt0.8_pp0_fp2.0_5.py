import weakref
from typing import Dict, Optional, Set, TYPE_CHECKING

import torch
import torch.nn as nn
from torch.jit.annotations import Dict, List, Optional, Tuple
from torch import Tensor, nn

if TYPE_CHECKING:
    from detectron2.modeling import GeneralizedRCNN

from .build import DETECTION_META_ARCH_REGISTRY
from .fast_rcnn import FastRCNNOutputLayers
from .postprocessing import detector_postprocess
from .roi_heads import ROI_HEADS_REGISTRY, StandardROIHeads
from .rpn import AnchorGenerator, RPNOutputLayers, RegionProposalNetwork
from .sampling import subsample_labels
from .backbone import build_backbone
from .build import META_ARCH_REGISTRY


@DETECTION_META_ARCH_REGISTRY.register()
class GeneralizedRCNN(nn.Module):
    """
    Main class for Generalized R-CNN. Currently supports boxes and masks.
    It consists of three main parts:
   
