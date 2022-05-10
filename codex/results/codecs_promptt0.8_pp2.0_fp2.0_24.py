import codecs
# Test codecs.register_error() :
#
# 1. Default
#
# 2. 'strict' mode, with and without register_error()
#
# 3. 'replace', with and without register_error()
#
# 4. 'ignore', with and without register_error()
#
# 5. 'strict' mode and register_error('strict', 'ignore')
#
# 6. 'replace' mode and register_error('replace', 'ignore')
#
# 7. 'ignore' mode and register_error('ignore', 'ignore')
#
# 8. 'strict' mode and register_error('strict', 'replace')
#
# 9. 'replace' mode and register_error('replace', 'replace')
#
# 10. 'ignore' mode and register_error('ignore', 'replace')
#
# 11. 'strict' mode and register_error('strict', 'xmlcharrefreplace')
#
# 12. 'replace' mode and register_error('replace', 'xmlcharrefreplace')
#
# 13. 'ignore' mode and register_error('ignore', 'xmlcharrefreplace')
