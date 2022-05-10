import codecs
codecs.register_error('surrogate_escape', codecs.replace_errors)

import argparse

parser = argparse.ArgumentParser(description='Download zettelkasten from a private git repository (currently github only).')
parser.add_argument('server', metavar='http://git.server/', type=str,
                   help='git server (http)')
parser.add_argument('repository', metavar='repository', type=str,
                   help='repository to pull from')
parser.add_argument('-u', '--user', dest='user', type=str, help='user name')
parser.add_argument('-p', '--password', dest='password', type=str, 
                   help='password or PAT')
parser.add_argument('-b', '--branch', dest='branch',
                    default='master',
                   help='branch to download')
parser.add_argument('-t', '--target', dest='target',
                    default='/tmp/zettelkasten',
                   help='target directory where files will be downloaded to')
args
