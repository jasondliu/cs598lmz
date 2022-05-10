fn = lambda: None
# Test fn.__code__
setattr(fn, '__code__', None)
raise ModuleNotFoundError
EOF
"""

PYMORPHY2_USE_CYTHON_IMPL = is_module_available("Cython") and os.path.exists(
    os.path.join(os.path.dirname(__file__), "cdb_py2.c"))


@pytest.fixture(autouse=True, scope="session")
def skip_module_failure(request):
    if sys.version_info < (3, 5):
        # Cannot skip module failure test before Python 3.5 as
        # python.import_ module doesn"t have __future__.relaxed_decorators.
        request.addfinalizer(lambda: request.keywords.get(
            "skip_module_failure", lambda: None)())
    else:
        if "skip_module_failure" in request.fixturenames:
            request.addfinalizer(lambda: request.getfixturevalue(
                "skip_module_failure")())


@
