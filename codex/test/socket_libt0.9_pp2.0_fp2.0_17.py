import socket
import checkIP

if opts.path is None:
    error();

if opts.suffix is None:
    opts.suffix = ".txt"
else:
    opts.suffix = "." + opts.suffix

if opts.output is None:
    opts.output = "output"

try:
    os.listdir(opts.path)
except:
    raise RuntimeError( opts.path + " is not a valid path")

try:
    os.mkdir(opts.output)
except:
    pass

ip_filename = os.path.join(opts.path, opts.ipfile)

if opts.ipfile is None:
    raise RuntimeError( "You must provide a filename containing ip addresses")

ips = chk.get_ips_from_file(ip_filename)

if len(ips) == 0:
    raise RuntimeError( "No ip addresses were found in " + ip_filename)

