import types
types.ModuleType('tensorflow').__file__

import tensorflow as tf

def tf_dataset_factory(dataset, is_training=False, batch_size=None, num_epochs=None, drop_remainder=None):
    """Factory for a new tensorflow Dataset object.
    Arguments:
      dataset: a Dataset object.
      is_training: boolean to indicate if the dataset is for training or eval.
      batch_size: the number of samples per batch.
      num_epochs: the number of times the dataset should be repeated.
      drop_remainder: a boolean, whether to drop the remainder of the batches.
    Returns:
      A Dataset object.
    """
    is_training = tf.constant(is_training, dtype=tf.bool)
    output_types = dataset.output_types
    output_shapes = dataset.output_shapes
    if batch_size is not None:
        output_shapes = output_shapes.as_list()
        output_shapes[
