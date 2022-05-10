import ctypes
ctypes.cast(0, ctypes.py_object)

# This is the only way to get a reference to the current interpreter.
# We need to store this in a global variable, so that we can pass it
# to other threads.
interpreter = sys.modules['__main__']

# The callback that is invoked by the IPython interactiveshell when
# user-code calls raw_input().
def raw_input_callback(prompt):
    # Ask the main thread for input.
    interpreter.raw_input_queue.put(prompt)
    # Wait for the main thread to send us a response.
    return interpreter.raw_input_queue.get()

# The callback that is invoked by the IPython interactiveshell when
# user-code calls input().
def input_callback(prompt):
    # Ask the main thread for input.
    interpreter.input_queue.put(prompt)
    # Wait for the main thread to send us a response.
    return interpreter.input_queue.get()

# This is the main thread.
def main():
    # Create the IPython kernel.
