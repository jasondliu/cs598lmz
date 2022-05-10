import ctypes
ctypes.cast(inputs, ctypes.c_void_p)

print("inputs: ", inputs, inputs.shape)
print("outputs: ", outputs, outputs.shape)

# The first way to load data into the network
# lib.network_load_batch(network, inputs, outputs)

# The second way to load data into the network
# ctypes.cast(inputs, ctypes.c_void_p)
# ctypes.cast(outputs, ctypes.c_void_p)
# lib.network_load_batch(network, inputs.ctypes.data_as(ctypes.c_void_p), outputs.ctypes.data_as(ctypes.c_void_p))

# The third way to load data into the network
# inputs_pointer, inputs_length = input_to_ctypes(inputs)
# outputs_pointer, outputs_length = input_to_ctypes(outputs)
# print("inputs_pointer: ", inputs_pointer, inputs_length)
# print("outputs_pointer: ", outputs_pointer, outputs_length)
#
