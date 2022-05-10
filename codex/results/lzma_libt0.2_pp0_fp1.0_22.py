import lzma
lzma.LZMAError

# This is a workaround for https://github.com/pypa/pip/issues/5240
# pip 10.0.1 is the first version that supports the `--no-binary` option
# to `pip install`.
if LooseVersion(pip.__version__) < LooseVersion('10.0.1'):
    raise RuntimeError('pip >= 10.0.1 is required')

# This is a workaround for https://github.com/pypa/pip/issues/5240
# pip 10.0.1 is the first version that supports the `--no-binary` option
# to `pip install`.
if LooseVersion(pip.__version__) < LooseVersion('10.0.1'):
    raise RuntimeError('pip >= 10.0.1 is required')

# This is a workaround for https://github.com/pypa/pip/issues/5240
# pip 10.0.1 is the first version that supports the `--no-binary` option
# to `pip install`.
