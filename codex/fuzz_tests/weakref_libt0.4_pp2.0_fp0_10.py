import weakref

import numpy as np
import scipy.sparse as sp

from Orange.data import Table, Domain, ContinuousVariable, DiscreteVariable
from Orange.data.util import get_unique_names
from Orange.preprocess import Discretize
from Orange.preprocess.continuize import DomainContinuizer
from Orange.statistics import distribution
from Orange.statistics.util import (
    get_distinct_values, get_distribution, get_contingency,
    get_contingency_with_indices, get_contingency_with_indices_and_weights,
    get_normalized_distribution, get_contingency_table,
    get_contingency_table_with_indices,
    get_contingency_table_with_indices_and_weights)
from Orange.util import Reprable, ReprableList, Enum
from Orange.util.cache import memoize_method
from Orange.util.lazy_module import LazyModule

__all__ = ["DomainTransformationError", "DomainTransformation",
           "Continu
