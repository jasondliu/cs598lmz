import sys, threading

def run():
    if len(sys.argv) < 2:
        print 'Usage: {} filename'.format(sys.argv[0])
        sys.exit()

    fname = sys.argv[1]
    a = datatypes.ATerminator(fname, features.ATerminator, MODE_PACK)
    a.run()
    print a
    a.save()

def run2():
    if len(sys.argv) < 2:
        print 'Usage: {} filename'.format(sys.argv[0])
        sys.exit()

    fname = sys.argv.pop()
    args = sys.argv
    args.append(fname)
    d = datatypes.Data()
    for i in range(0, len(args)):
        if not args[i].startswith('-'):
            continue
        if args[i] == '-m':
            d.append(datatypes.DPanel(args[i+1], MODE_MAP, d.objects[-1]))
        elif
