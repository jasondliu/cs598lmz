import mmap,subprocess,time,tempfile,shutil,os,logging
from pdb import set_trace as st

def get_paths(d):
    uri = d['uri']
    if 'file://' in uri:
        d['uri'] = uri[len('file://'):]
    elif 'file:\\' in uri:
        uri = uri[len('file:\\'):]
        d['uri'] = uri.replace('\\','/')
    else:
        logging.error('UNKNOWN uri format: "{}"'.format(uri))
        raise ValueError('UNKNOWN uri format')
    d['uri'] = os.path.abspath(d['uri'])
    if 'local_workspace_path' in d:
        d['local_workspace_path'] = os.path.abspath(d['local_workspace_path'])

def build_workspace(d,paths):
    try:
        os.makedirs(paths['local_workspace_path'])
   
