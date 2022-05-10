import codecs
codecs.register_error('replace_non_compliant_unicode_surrogates',
                      replace_non_compliant_unicode_surrogates)

@contextmanager
def replace_non_compliant_unicode_surrogates_context(new_value):
    """
    Context manager that replaces all non compliant unicode surrogates by the
    new value.
    """
    old_value = codecs.lookup_error('replace_non_compliant_unicode_surrogates').replace_with
    codecs.lookup_error('replace_non_compliant_unicode_surrogates').replace_with = new_value
    yield
    codecs.lookup_error('replace_non_compliant_unicode_surrogates').replace_with = old_value
