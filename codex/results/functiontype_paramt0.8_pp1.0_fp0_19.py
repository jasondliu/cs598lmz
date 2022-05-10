from types import FunctionType
list(FunctionType(code) for code in codes)

# (1) get PEP8 doc from bytecode
# (2) compare with original
# (3) compare with generated with pep8 checker
# (4) extra check for issues with pep8 checker
# (5) output issues to terminal
# (6) output issues to file
# (7) add support for spaces in file names
# (8) add pytest coverage

# Improve PEP8 checks
# ** skip lines like "async def"
# ** add support for # noqa
# ** add option to continue if error
# parse PEP8 doc
# ** add color to output
# ** add support for various output format
