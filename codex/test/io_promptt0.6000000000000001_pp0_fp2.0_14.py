import io
# Test io.RawIOBase
# Test io.BufferedIOBase
# Test io.TextIOBase

# Test io.StringIO on Py2 and Py3
try:
    # Py3
    import io
    from io import StringIO
    from io import BytesIO
except ImportError:
    # Py2
    import StringIO as io
    from StringIO import StringIO
    from io import BytesIO

# Test io.BytesIO on Py2 and Py3
try:
    # Py3
    import io
    from io import BytesIO
except ImportError:
    # Py2
    import io
    from io import BytesIO

# Test io.BytesIO on Py2 and Py3
try:
    # Py3
    import io
    from io import BytesIO
except ImportError:
    # Py2
    import io
    from io import BytesIO

# Test io.BytesIO on Py2 and Py3
try:
    # Py3
    import io
    from io import BytesIO
except ImportError:
    # Py2
    import io
