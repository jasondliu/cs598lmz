import bz2
bz2_model = JoblibPackage(bz2_path, bz2.decompress, bz2.compress)

# module level attribute
__SCHEMA_VERSION__ = 'v1.0'

# basic type value
_BINARY_FORMAT_VERSION = 0

# classes and attributes
RealReader = _RealReader
RealDumper = _RealDumper
RealFormat = _RealFormat
JoblibPackage = _JoblibPackage

# joblib compatible functions
load = JoblibPackage.load
dump = JoblibPackage.dump

# for extension purpose
__all_formats__ = [
    bz2_model,
    cmp_model,
    gz_model,
    lzma_model,
    raw_model,
    zip_model
]

# endregion


# region File utility

def _standardize_path(filename):
    filename = os.path.abspath(filename)
    if os.sep == '\\':
        return filename.replace('/', os.sep)
    return filename


class _
