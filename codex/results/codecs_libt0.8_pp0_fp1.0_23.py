import codecs
codecs.register(amr_reader.search)

# Populate the "__version__" string.
#   See https://packaging.python.org/en/latest/single_source_version.html
#   See https://github.com/pypa/warehouse/blob/master/warehouse/packaging/__init__.py
try:
    from importlib.metadata import version, PackageNotFoundError  # type: ignore
except ImportError:  # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError  # type: ignore


try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
