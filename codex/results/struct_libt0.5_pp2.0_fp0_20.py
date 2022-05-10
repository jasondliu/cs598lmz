import _struct

from pytest import raises
from itertools import product

from hypothesis import given
from hypothesis.strategies import integers, lists, composite

from .strategies import (
    lists_strategies,
    iterables_strategies,
    numbers_strategies,
    single_numbers_strategies,
    non_negative_numbers_strategies,
    single_non_negative_numbers_strategies,
    non_empty_numbers_strategies,
    single_non_empty_numbers_strategies,
    non_negative_integers_strategies,
    single_non_negative_integers_strategies,
    non_empty_integers_strategies,
    single_non_empty_integers_strategies,
    non_negative_floats_strategies,
    single_non_negative_floats_strategies,
    non_empty_floats_strategies,
    single_non_empty_floats_strategies,
    non_negative_complexes_
