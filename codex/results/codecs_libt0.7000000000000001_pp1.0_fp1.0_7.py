import codecs
codecs.getwriter('utf8')(sys.stdout)

import json

try:
    import requests
except ImportError:
    print "This script requires the 'requests' library. Please install this library and try again."
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Check if a given file is being cached by Cloudflare", epilog="""
This script checks if a file is being cached by Cloudflare.
It will exit with a return code of 1 if the file is not
cached. Any other return code is an error.
""")
    parser.add_argument('--url', dest='url', required=True,
                        help='URL of the file to check')
    parser.add_argument('--zone', dest='zone', required=True,
                        help='Zone Name of the file to check')
    parser.add_argument('--email', dest='email', required=True,
                        help='Cloudflare account email address')
    parser.add_argument('--token', dest='token', required=True,
                       
