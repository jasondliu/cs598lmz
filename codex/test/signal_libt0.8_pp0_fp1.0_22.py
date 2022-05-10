import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def parse_Line(frame_Line):
    kv = [x.split(':') for x in frame_Line.split('\t')]
    return {z[0].strip(): z[1].strip() for z in kv}

def parse_File(fileName):
    #return [(t,x,y) for line in open(fileName) for t,x,y in [parse_Line(line).items()]]
    return [parse_Line(line) for line in open(fileName)]

def convert_File(fileName):
    #return [(t,x,y) for line in open(fileName) for t,x,y in [parse_Line(line).items()]]
    return [str(parse_Line(line)) for line in open(fileName)]

def save_File(fileName, data):
    with open(fileName, 'a') as f:
        for d in data:
            f.write(d + '\n')

