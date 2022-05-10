import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
#import gzip
#import os
import cPickle

sys.stderr = sys.stdout

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web2py.settings")

#from django import db
#db.connections.close_all()

try:
    from gluon.custom_import import custom_import_install
    custom_import_install('w2p_datastore')
except:
    pass

#try:
#    import settings
#except ImportError:
#    import os
#    sys.path.append(os.path.abspath('..'))
#    import settings
#import os, sys
#sys.path.append(os.path.join(os.path.abspath(''), 'applications'))


#def run(app, host='127.0.0.1', port=80):
#    from wsgiref.simple_server import
