gi = (i for i in ())
# Test gi.gi_code (pure-code for-loop generator)
gi.gi_code

# Check that we get a warning in this case, see bugs.python.org/issue12587
with check_py3k_warnings(
    DeprecationWarning,
    "the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses"
):
    import imp

# Importing "PIL.Image" results in a DeprecationWarning, see bugs.python.org/issue15326

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning,
                            message="The 'warn' method is deprecated, use 'warning' instead")
    from PIL import Image

image = Image.Image()
image.warn("some message")
