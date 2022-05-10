import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.fd = open(filename, "rb")

    def read(self, size=-1):
        return self.fd.read(size)

    def seek(self, offset, whence=0):
        return self.fd.seek(offset, whence)

    def close(self):
        return self.fd.close()
import cv2
from PIL import Image
from torchvision import transforms
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import numpy as np

from model.model_seg import Model
from utils.util import decode_segmap
from config import *


class SegModel(Model):
    def __init__(self, model_path, device, num_classes, img_size):
        super(SegModel, self).__init__(model_path, device)
        self.num_classes = num_classes
        self.img_size = img_size

    def preprocess(self, img):
        img = img.resize((self.img_size
