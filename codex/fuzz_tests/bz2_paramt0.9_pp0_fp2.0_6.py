from bz2 import BZ2Decompressor
BZ2Decompressor().flush()

def _string_record_reader(record):
  """Take a single serialized string and return the tensors."""
  fields = tf.io.decode_csv(record, [tf.constant([], dtype=tf.string)] * 9)
  encoded_image = fields[0]
  image_format = fields[1]
  height = tf.cast(tf.strings.to_number(fields[2], tf.int32), tf.int32)
  width = tf.cast(tf.strings.to_number(fields[3], tf.int32), tf.int32)
  depth = tf.cast(tf.strings.to_number(fields[4], tf.int32), tf.int32)
  bboxes = tf.stack([
      tf.cast(tf.strings.to_number(fields[6], tf.float32), tf.float32),
      tf.cast(tf.strings.to_number(fields[5], tf.float32), tf.float32),
      tf.cast(tf.strings.to_number(fields[8],
