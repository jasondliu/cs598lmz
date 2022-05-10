import ctypes
ctypes.cdll.LoadLibrary('caffe2_nvrtc.dll')
ctypes.cdll.LoadLibrary('caffe2_gpu_kernels.dll')



from caffe2.python import workspace, core, rnn_cell, rnn_recurrent_utils
from caffe2.python.rnn.rnn_recurrent_utils import LSTMState, LSTMStateTuple
from caffe2.python.rnn.rnn_recurrent_utils import char_sequence_to_padded_index_sequence, padded_index_sequence_to_char_sequence
from caffe2.python.rnn.rnn_recurrent_utils import get_char_sequence_lengths, get_char_sequence_lengths_from_padded_index_sequence
from caffe2.python.rnn.rnn_recurrent_utils import LSTMState, LSTMStateTuple
from caffe2.python.rnn.rnn_recurrent_utils import bi_lstm_transform_input, bi_lstm_transform_input_with_weight_projection
from caffe2.
