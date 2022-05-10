import codecs
# Test codecs.register_error("strict", codecs.ignore_errors)

from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
from setuptools.command.test import test

from Cython.Build import cythonize


class BuildExt(build_ext):
    def run(self):
        from Cython.Build import cythonize
        cythonize(self.extensions)
        super().run()


class PyTest(test):
    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)


ext_modules = [
    Extension(
        'pygls.features',
        ['pygls/features.pyx'],
        include_dirs=[np.get_include()]
    ),
    Extension(
        'pygls.utils',
        ['pygls/
