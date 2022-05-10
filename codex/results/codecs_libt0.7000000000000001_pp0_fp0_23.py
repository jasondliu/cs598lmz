import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# XML Paths
#
# Paths to the XML files for the different packages for the different languages.
# They are used to check whether the package exists and how many strings are in it.
xml_path = {
    'en': {
        'base': '../client_en/en.po',
        'base_xml': '../client_en/en.xml',
        'base_xml_count': '../client_en/en_count.xml',
        'base_xml_missing': '../client_en/en_missing.xml',
        'base_xml_extra': '../client_en/en_extra.xml',
        'base_xml_diff': '../client_en/en_diff.xml',
        'base_xml_diff_count': '../client_en/en_diff_count.xml',
        'client_en': '../client_en/client_en.po',
        'client_en_xml': '../client
