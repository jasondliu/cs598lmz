import types
types.ModuleType.__repr__ = module_repr

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

import model


def print_table(model):
    print('.L-layer-%d, n_features=%d' % (model.num_layers,
                                          model.layers[0].n_features))
    print(' tr_err %0.4f' % model.tr_err)
    print(' val_err %0.4f' % model.val_err)
    print(' test_err %0.4f' % model.test_err)

    try:
        for layer in model.layers:
            print(layer)

        for i, weights in enumerate(model.weights):
            print()
            print('weights')
            print('weights[' + str(i) + '].shape ' + str(weights.shape))
            print('min max %f %f' % (np.min(weights), np
