import _struct
import inspect
import itertools
import math
import numpy as np
import os
import six
import sys
import tensorflow as tf

# The class and methods in this module are abstractions of the high-level APIs
# provided by the TensorFlow team. The original version of this code is found
# in the TensorFlow GitHub repository.
#
# This module is based off the code in:
# https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/profiler/internal/flops_registry.py
#
# The license below is from the TensorFlow repository:
#
# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed
