import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
        def __enter__(self):
            a.append(self)
        def __exit__(self, exc_type, exc_value, exc_tb):
            a.pop()
        def __del__(self):
            test_select_mutated()

    select.select([F()], [], [])

    class F:
        def fileno(self):
            return object()
        def __enter__(self):
            pass
        def __exit__(self, exc_type, exc_value, exc_tb):
            pass

    select.select([F()], [], [])

LDAPError = int

def test_ldap_null_sock(LDAPError):
    class LDAPObject:
        def unbind(self): pass
    def ldap_initialize(x):
        if not getattr(ldap_initialize, 'raise_exception', False):
            ldap_initialize.raise_exception = True
            return LDAPObject()
        raise LDAPError()
    LDAPObject.initialize =
