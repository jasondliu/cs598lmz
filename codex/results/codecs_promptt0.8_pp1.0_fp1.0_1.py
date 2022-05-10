import codecs
# Test codecs.register_error( '_not-i18n_', lambda e: ( "", e.end ) )

# x12 = 'ABCD1234'
# Test x13 = x12.translate( codecs._not-i18n_ )
# Test assert x13 == u''
# Test assert ( x13, len(x12) ) == codecs._not-i18n_( UnicodeTranslateError( 'ABCD1234', 0, 4, "i-18n string" ) )

# Test codecs.register_error( '_not-i18n_', codecs.replace_errors )
# Test x14 = x12.translate( codecs._not-i18n_ )
# Test assert x14 == u'????'
# Test assert ( x14, len(x12) ) == codecs._not-i18n_( UnicodeTranslateError( 'ABCD1234', 0, 4, "i-18n string" ) )


# Test codecs.register_error( '_not-i18n_', lambda e: ( u"?", e.end ) )
# Test
