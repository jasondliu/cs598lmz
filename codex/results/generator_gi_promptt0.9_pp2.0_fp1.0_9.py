gi = (i for i in ())
# Test gi.gi_code (code of gi)
if not hasattr(gi, 'gi_code'):
    raise TestFailed("Subgenertor without its own code object doesn't have gi_code attribute")
gi_code = gi.gi_code
if not isinstance(gi_code, types.CodeType):
    raise TestFailed("gi_code is not a code object")
if not hasattr(gi_code, 'co_filename') or not hasattr(gi_code, 'co_name'):
    raise TestFailed("code object of subgenerator doesn't have co_filename or co_name attribute")
gi_filename = gi_code.co_filename
gi_name = gi_code.co_name
if not isinstance(gi_filename, str):
    raise TestFailed("gi_code.co_filename is not a string")
if gi_filename == '<stdin>':
    raise TestFailed("gi_code.co_filename is not set")
if not isinstance(gi_name, str):
    raise TestFailed("gi_code.co_
