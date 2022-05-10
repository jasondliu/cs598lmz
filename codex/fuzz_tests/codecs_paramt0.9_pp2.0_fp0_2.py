import codecs
codecs.register_error(
    'strict', codecs.ignore_errors)

def setup(app):
    app.connect('builder-inited', run_apidoc)

def clean(app, exc):
    if exc:
        return
    run_apidoc('clean', app)

def run_apidoc(what, app=None):
    here = os.path.abspath(os.path.dirname(__file__))
    srcdir = os.path.join(here, '../src')
    outdir = os.path.join(here, 'apidocs')

    gen = ['sphinx-apidoc', '-H', 'Ubiwhere Python SDK/*', '-V',
           '0.1.0', '-o', outdir, srcdir]

    if what == 'clean':
        gen.append('--force')

    try:
        subprocess.check_call(gen)
    except Exception as e:
        print('An error happened while running sphinx-apidoc')
        raise e
