import gc, weakref

from . import _cffi_backend


@contextlib.contextmanager
def _empty_contextmgr():
    yield

_cffi1_lock = _empty_contextmgr()
if _cffi_backend.__name__ == '_cffi_backend_cffi_mirror':
    import _cffi_backend_cffi_mirror
    _cffi1_lock = _cffi_backend_cffi_mirror._cffi1_lock


def _copy_cffi_struct_layout(src, dst):
    """Copy the layout of a struct from src to dst.

    It assumes that dst has the same size as src, and will copy the
    fields in the same order.  Note that this is *not* a general
    function: it is only useful for the specific case of copying the
    layout of a cffi1 _cffi_backend.CType instance.
    """
    # XXX this function is a bit ugly, but it is the easiest way to
    # copy
