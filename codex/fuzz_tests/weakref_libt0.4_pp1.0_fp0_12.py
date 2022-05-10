import weakref

from . import _util
from . import _pytest

class Test_pytest_addoption(object):
    def test_addoption(self, testdir):
        testdir.makepyfile("""
            import pytest
            def pytest_addoption(parser):
                parser.addoption("--hello", action="store", default=123,
                    help="set greeting")
            def test_option(request):
                assert request.config.getvalue("hello") == "world"
        """)
        result = testdir.runpytest("--hello=world")
        result.stdout.fnmatch_lines([
            "*1 passed*",
        ])

    def test_addoption_issue137(self, testdir):
        testdir.makepyfile("""
            import pytest
            def pytest_addoption(parser):
                parser.addoption("--hello", action="store", default=123,
                    help="set greeting")
            def test_option(request):
                assert request.config.getvalue("hello") == 123
        """)
       
