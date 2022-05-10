import codecs
codecs.register_error('strict', codecs.replace_errors)

# Global variables

GLOBAL = dict()

def initGlobalVariables(conf):
    global GLOBAL
    GLOBAL['WORKING_DIRECTORY'] = conf.get('working_directory', '.')
    GLOBAL['OUTPUT_DIRECTORY'] = conf.get('output_directory', '.')
    GLOBAL['TMP_DIRECTORY'] = conf.get('tmp_directory', '.')
    GLOBAL['TEMPLATE_DIRECTORY'] = conf.get('template_directory', '.')
    GLOBAL['STATIC_DIRECTORY'] = conf.get('static_directory', '.')
    GLOBAL['LANGUAGES'] = conf.get('languages', ['en', 'fr'])
    GLOBAL['MAIN_LANGUAGE'] = conf.get('main_language', 'en')
    GLOBAL['DEFAULT_LANGUAGE'] = conf.get('default_language', 'en')
    GLOBAL['CONTENT_URL
