import lzma
lzma.LZMAError

# lzma module is optional
# pylint: disable=E0611

# -----------------------------------------------------------------------------
#
# The following code implements a class that can be used to read and write
# LZMA compressed files.
#
# The code is derived from the LZMAFile class in the Python 3.3 standard
# library.  The original code is:
#
#   Copyright (c) 2001-2010 Python Software Foundation; All Rights Reserved
#
#   Copyright (c) 2001-2010 Igor Pavlov.  All Rights Reserved.
#
#   Copyright (c) 2000-2001 Joel de Guzman.  All Rights Reserved.
#
#   Copyright (c) 1995-2001 Corporation for National Research Initiatives.
#       All Rights Reserved.
#
#   Copyright (c) 1991-1995 Stichting Mathematisch Centrum.  All Rights
#       Reserved.
#
# The changes made to the original code are:
#
#   - The code has been modified to work with Python 2.7.
#
#   - The code has been modified to work with older versions of the
