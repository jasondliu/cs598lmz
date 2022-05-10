import weakref

from falcon import request_helpers
from falcon.util import uri

# NOTE(kgriffs): Import for side-effect of adding submodule to this package.
import falcon.request_helpers.multipart  # noqa

from .util import get_query_param
from .util import get_text_reader

# --------------------------------------------------------------------
# Exceptions
# --------------------------------------------------------------------


class HTTPBadRequest(Exception):
    """Used for HTTP 400 errors that require a response body.

    For example, a request contains invalid parameters that can be
    safely interpreted by the API.

    """


# --------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------

def _format_types_and_desc(req, resp):
    """Returns the formatted ``type`` and ``description`` of a parameter
    using a Request instance and Response instance.
    """

    types = req.get_param_types(resp.name)
    if types:
        if len(types) == 1:
            type_ = types[0]
        else:
            type_ = ', '.join("'%s'" %
