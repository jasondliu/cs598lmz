import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

from collections import OrderedDict

from pdfrw import PdfReader, PdfWriter


def handle(infile, params):
    
    if infile == '-':
        infile = sys.stdin.buffer
    else:
        infile = open(infile, 'rb')

    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    if params.suffix:
        outfile = infile.name + params.suffix
    else:
        outfile = infile.name

    writer = PdfWriter()
    reader = PdfReader(infile)

    file_info = OrderedDict(reader.Info)
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    if params.change_xmp:
        file_info['/Keywords'] = params.change
