import weakref
from sys import float_info

from . import _libsvm
from . import _liblinear
from . import _libsgd
from . import _liblinear_dataset
from . import _libsgd_dataset
from . import _libsvm_dataset
from . import _libsvm_sparse
from . import _liblinear_sparse
from . import _libsgd_sparse
from . import _dataset_ops

from . import _exceptions
from . import _sparsetools
from . import _sparseformat
from . import _preprocess
from . import _svmlight_format
from . import _svmlight_loader
from . import _svmlight_saver
from . import _svmlight_file_ops
from . import _svmlight_converter
from . import _sparse_dataset_ops

from ._libsvm_sparse import (
    svm_read_problem, svm_read_problem_from_string,
    svm_load_model, svm_load_model
