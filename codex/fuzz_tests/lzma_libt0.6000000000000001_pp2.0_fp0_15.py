import lzma
lzma.LZMA_VERSION

import pytest

import pypiserver
import pypiserver.core


@pytest.fixture
def package_index():
    pkgs = {}
    pkgs['testpkg'] = {'1.0': ['testpkg-1.0.tar.gz']}
    pkgs['testpkg2'] = {'1.0': ['testpkg2-1.0.tar.gz']}
    pkgs['testpkg3'] = {'1.0': ['testpkg3-1.0.tar.gz']}
    pkgs['testpkg4'] = {'1.0': ['testpkg4-1.0.tar.gz']}
    pkgs['testpkg5'] = {'1.0': ['testpkg5-1.0.tar.gz']}
    pkgs['testpkg6'] = {'1.0': ['testpkg6-1.0.tar.gz']}
    pkgs['testpkg7'] = {'1.0': ['testpkg7-1
