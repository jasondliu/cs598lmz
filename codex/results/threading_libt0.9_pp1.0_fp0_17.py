import threading
threading.Thread(target=lambda: tf.nn.dynamic_rnn(
    cell=lstm_fw_cell_1,
    inputs=inputs,
    dtype=tf.float32,
    sequence_length=X_lengths,
    parallel_iterations=32,
)).start()
threading.Thread(target=lambda: tf.nn.dynamic_rnn(
    cell=lstm_bw_cell_1,
    inputs=inputs[::-1, :, :],
    dtype=tf.float32,
    sequence_length=X_lengths,
    parallel_iterations=32,
)).start()
</code>

