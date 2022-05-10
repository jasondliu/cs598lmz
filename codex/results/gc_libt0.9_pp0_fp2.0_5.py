import gc, weakref

##### Private globals #####

# A dict mapping the values of the enumerated 'disp' property to their
# corresponding arrow drawing function.
_arrow_funcs = {'none': lambda coord, x, y, ax: None,
                'last': _draw_last_arrow,
                'first': _draw_first_arrow,
                'both': _draw_both_arrows,
                'angle': _draw_angle_arrow}

# Map input values to the correct transform. This is to support the
# normal axes coordinate system, which is 0,0 in the lower left corner
# with the positive x-axis going right, but positive y-axis going up
# Mobular transform works differently
_transform_xs = {
    'data': 'data',
    'axes': 'data',
    'polar': 'polar',
    'datalimited': 'datalimited'
}
_transform_ys = {
    'data': 'data',
    'axes': 'axes',
    'polar': 'polar',
    'datalimited
