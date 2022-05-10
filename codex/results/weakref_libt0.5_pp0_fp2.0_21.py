import weakref
import contextlib
import functools
import inspect
import logging

import numpy as np

from . import core
from . import utils

__all__ = ['DenseDesignMatrix', 'DesignMatrix', 'dataset_yielder',
           'dataset_resampler', 'dataset_percenter',
           'dataset_bootstrapper', 'dataset_averager',
           'dataset_multitransformer', 'dataset_postprocessor',
           'Dataset', 'DatasetIterator', 'DenseDesignMatrixPyTables',
           'DenseDesignMatrixHDF5', 'DenseDesignMatrixCSV',
           'DenseDesignMatrixSVMLight', 'SparseDesignMatrix',
           'SparseDesignMatrixPyTables', 'SparseDesignMatrixCSV',
           'SparseDesignMatrixSVMLight', 'IndexableDataset',
           'IndexableDatasetIterator', 'IndexIterator', 'IndexableDataset',
           'IndexableDatasetIterator', 'IndexIterator', 'DenseDesignMatrix',
