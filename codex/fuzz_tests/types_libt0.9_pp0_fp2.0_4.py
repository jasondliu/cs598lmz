import types
types.ModuleType = ModuleType

import torch
from torch import nn
from torch.nn import functional as F

from base import BaseModel
from core import constants as Constants


class Generator(nn.Module):
    """
    There is two layer of 1D convolution with kernel size
    3, and padding size as 1.
    """

    def __init__(self,
                 input_size,
                 board_width,
                 board_height,
                 residual_channels):
        super(Generator, self).__init__()
        self.input_size = input_size
        self.residual_channels = residual_channels
        self.board_width = board_width
        self.board_height = board_height
        self.inplanes = input_size
        self.planes = residual_channels

        self.block1 = ResidualConvUnit(
            in_channels=self.inplanes,
            out_channels=self.planes,
            kernel_size=3
        )
        self.block2 = ResidualConvUnit(

