import io
# Test io.RawIOBase.tell()
from _io import RawIOBase

from itertools import permutations, combinations
from sys import stderr  # noqa
from multiprocessing import Pipe  # noqa


@pytest.fixture
def N():
    return 1, 2, 5


@pytest.fixture
def sym_func(N, beta, clazz):
    energies = np.arange(clazz.N_k(N[-1])) * beta
    weights = np.exp(-beta * energies)
    return clazz(N, energies=energies, weights=weights, nsamp=20), energies


@pytest.fixture
def nonsym_func(N, beta, clazz):
    energies = np.arange(clazz.N_k(N[-1])) * beta
    weights = np.exp(-beta * energies)
    return clazz(N, energies=energies, weights=weights, nsamp=20, permute=False), energies


def test_sample_shapes_sym(sym_func, beta):
    f,
