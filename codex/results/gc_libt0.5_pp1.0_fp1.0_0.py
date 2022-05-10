import gc, weakref

import numpy as np

from . import _bvpl_octree_batch, _bvpl_octree_batch_vector
from .. import boxm2_batch, boxm2_batch_adaptor
from ..boxm2_batch import *
from ..boxm2_batch_adaptor import *

#############################################################################
# batch wrapper functions
#############################################################################


def load_scene(filename, use_gpu=True):
    if not use_gpu:
        return boxm2_batch.load_scene(filename)
    else:
        batch.init_process("bvplLoadSceneProcess")
        batch.set_input_string(0, filename)
        batch.run_process()
        (scene_id, scene_type) = batch.commit_output(0)
        scene = dbvalue(scene_id, scene_type)
        return scene


def scene_info(scene):
    batch.init_process("bvplSceneInfoProcess")
    batch.set_input_from_db(0, scene)
    batch.run
