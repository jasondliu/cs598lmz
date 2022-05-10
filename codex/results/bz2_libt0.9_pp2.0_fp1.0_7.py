import bz2
bz2.BZ2File = BZ2Compressor
# bz2_file stands for a bz2 file handle

# gzip
import gzip
import io
gzip.GzipFile = GnuZipCompressor
# f_in stands for a gzip file handle

# Ensure all network io is in binary mode
assert sys.version_info >= (3,)

export_by_req = True

def serve(port_number, hostname=None):
    if hostname is None:
        if port_number == 80:
            hostname = "www.vpn.net"
        else:
            hostname = "localhost"

    httpd = HTTPServer((hostname, port_number), RequestHandler)
    print("""
Server = {}
Port = {}
""".format(hostname, port_number))
    user_interrupt = False
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        user_interrupt = True
    except:
        (etype, value, tb) = sys.exc_info()
       
