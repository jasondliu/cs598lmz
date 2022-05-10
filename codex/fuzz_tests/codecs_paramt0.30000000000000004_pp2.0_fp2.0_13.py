import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-----------------------------------------------------------------------------
#  Copyright (C) 2013 The IPython Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

from IPython.utils.traitlets import Unicode, Bool, Dict, List
from IPython.utils.importstring import import_item

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------

class NotebookNotary(object):
    """A class for computing and checking notebook signatures.
    
    This class is used to compute the signatures of notebooks.  These signatures
    are used to check the integrity of notebooks when they are opened.
    """
    # The algorithm used to sign notebooks.
    algorithm = Unicode(u'sha1', config=True, help="""
        The algorithm used to generate notebook signatures.
        """
    )
    # The secret key with which notebooks are signed.
    secret = Unicode(u'', config=True,
