import weakref

from . import _util
from . import _compat
from . import _core
from . import _ffi
from . import _lib
from . import _types
from . import _winapi


class _BaseCredential(object):
    """Base class for credentials."""

    def __init__(self, cred_type):
        self._cred_type = cred_type

    def _get_credential(self):
        """Return a new Credential object."""
        raise NotImplementedError

    def _get_credential_handle(self):
        """Return a new CredentialHandle object."""
        cred = self._get_credential()
        return _core.CredentialHandle(cred)

    def _get_credential_handle_for_sspi(self, target_name):
        """Return a new CredentialHandle object for SSPI."""
        cred = self._get_credential()
        return _core.CredentialHandleForSSPI(cred, target_name)


class _C
