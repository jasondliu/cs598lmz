gi = (i for i in ())
# Test gi.gi_code.co_flags & CO_GENERATOR
if not (gi.gi_code.co_flags & 4):
    # Python 3.2 - 3.5
    gen.throw = _throw
    gen.close = _close


def _add_base(cls, base):
    if isinstance(base, str):
        base = import_module(base)

    # code borrowed from
    #     https://github.com/google/python-gflags/blob/master/python/gflags/__init__.py#L1320
    #     - oauth2client/contrib/gflags.py
    #     - kazoo/security/gssapi.py
    #     - gssapi/raw.py
    #     - flask/app.py
    #     - gunicorn/workers/ggevent.py
    #     - gevent/monkey.py
    #     - blinker/base.py
    #     - celery/utils/__init__.py
    #     - django/forms/__init__.py
    if has
