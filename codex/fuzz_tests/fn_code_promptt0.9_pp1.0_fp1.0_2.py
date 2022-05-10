fn = lambda: None
# Test fn.__code__
if hasattr(fn, '__code__'):
    # Cython
    def num_args(func):
        return func.__code__.co_argcount
else:
    # Python
    def num_args(func):
        return len(inspect.signature(func).parameters)

def to_categorical_inplace(Y, n_classes):
    new_Y = np.zeros((Y.shape[0], n_classes))
    new_Y[np.arange(Y.shape[0]), Y] = 1.0
    np.copyto(Y, new_Y)
    return Y

def get_output_shape(model, input_shape):
    if isinstance(input_shape, int):
        output_shape = 1
        for layer in model.layers:
            if 'Flatten' in layer.get_config()['name']:
                continue
            elif 'InputLayer' in layer.get_config()['name']:
                output_shape *= layer.input_shape[1]
            else:

