import ctypes
ctypes.cast(mem_block, ctypes.py_object).value

#%%
import numpy as np
def generate_data(n_samples, n_features=2, n_informative=2, n_redundant=0,
                  n_repeated=0, n_classes=2, n_clusters_per_class=2,
                  weights=None, flip_y=0.01, class_sep=1.0, hypercube=True,
                  shift=0.0, scale=1.0, shuffle=True, random_state=None):
    generator = check_random_state(random_state)
    if weights and len(weights) != n_classes:
        raise ValueError("Weights vector (%d) does not match number of classes "
                         "(%d)" % (len(weights), n_classes))

    if hypercube:
        corners = np.array([shift] * n_features * n_classes)
        shifts = np.identity(n_features) * class_sep
        for k in range(n_classes - 1):
            corners
