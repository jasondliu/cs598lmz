import codecs
codecs.register_error('ignore', lambda x: ' ')

# remove the --no-update tag
# if '--no-update' in sys.argv:
#     sys.argv.remove('--no-update')

setup(
    name = 'pydatajson',
    version = '2.5.0',
    description = 'Librería para la validación y consumo de un data.json',
    author = 'Datos Argentina',
    author_email = 'datos@modernizacion.gob.ar',
    url = 'https://github.com/datosgobar/pydatajson',
    # download_url = 'https://github.com/datosgobar/pydatajson/tarball/0.1.0',
    keywords = ['data.json', 'api', 'catalog', 'metadata'],
    packages=['pydatajson',
              'pydatajson.utils',
              'pydatajson.readers',
              'pydatajson.readers.csv',
              'pydatajson.readers.xlsx',
