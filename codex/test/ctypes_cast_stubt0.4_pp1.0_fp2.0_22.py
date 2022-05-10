import ctypes
ctypes.cast(0, ctypes.py_object)

# Enable pytest-cov plugin
# https://pytest-cov.readthedocs.io/en/latest/
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "cov: measure coverage"
    )

def pytest_addoption(parser):
    parser.addoption(
        "--cov", action="store_true", default=False, help="run coverage"
    )
    parser.addoption(
        "--cov-report", action="store", default=None,
        help="generate a coverage report, defaults to term-missing"
    )
    parser.addoption(
        "--cov-config", action="store", default=None,
        help="config file for coverage, defaults to .coveragerc"
    )

def pytest_collection_modifyitems(config, items):
    if config.getoption("--cov"):
        import pytest
