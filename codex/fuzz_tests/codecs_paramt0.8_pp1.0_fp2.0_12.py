import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

def _compute_seq_length(text, max_size):
    text_size = tf.size(text)
    max_size = tf.maximum(max_size, tf.constant(1, dtype=tf.int64))
    seq_len = tf.minimum(
        tf.maximum(
            tf.cast(tf.ceil(text_size/(max_size+1)), tf.int64),
            tf.constant(1, dtype=tf.int64)
        ),
        tf.constant(128, dtype=tf.int64)
    )
    return text_size, seq_len

def _prepare_text(text):
    max_size = tf.constant(1024, dtype=tf.int64)
    text = tf.reshape(text, (-1,))
    text_size, seq_len = _compute_seq_length(text, max_size)
    text = tf.cond(text_size > max_size, lambda:
