import mmap

from tensorflow.python.framework import errors
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import gen_array_ops

from ixa.sys.ixa_ptr_gen.inference import infer_model_ops
from ixa.sys.ixa_ptr_gen.inference import model_helper
from ixa.sys.ixa_ptr_gen.inference import vocab_mgr_ops


def get_global_step(sess):
    """Return the current global_step value."""
    return sess.run(model.global_step)


# The way to restore the parameters.
# ckpt = tf.train.get_checkpoint_state(FLAGS.model_dir)
# self.model_infer = infer_model_ops.create_model(self.model_hparams, ckpt.model_checkpoint_path, train=False)

class PTRGenModel(object):
    """Sequence-to-sequence dynamic model.

    This class implements a multi-layer
