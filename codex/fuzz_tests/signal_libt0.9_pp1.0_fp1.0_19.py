import signal
signal.signal(signal.SIGINT, signal.SIG_DFL) # avoid process termination
mgr = ProjectManager()


#
#
#

def symlink_dir(dir_source, dir_dest):
    if not os.path.exists(dir_dest):
        os.mkdir(dir_dest)

    for f in os.listdir(dir_source):
        src, ext = os.path.splitext(os.path.abspath(os.path.join(dir_source, f)))

        if ext.lower() == '.ipynb':
            return mgr.symlink(src, os.path.join(dir_dest, '%s.html' % f))


#
# Link all ipynbs in a directory
#

ipynbs_src = os.path.abspath('ipynb')
ipynbs_dest = os.path.abspath('docs/_static/ipynb')
os.system('rm -rf %s' % ipynbs_dest)
os.mkdir(ip
