import codecs
codecs.register_error('strict', codecs.ignore_errors)

# The version of the wrapped library is the starting point for the
# version number of the python package.
# In bugfix releases of the python package, add a '-' suffix and an
# incrementing integer.
# For example, a packaging bugfix release version 1.4.4 of the
# js.jquery package would be version 1.4.4-1 .

version = '1.0.0'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'jquery_ui_slider', 'test_jquery_ui_slider.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jquery_ui_slider',
    version=version,
    description="Fanstatic packaging of jQuery UI Slider",
    long_description=
