import codecs
codecs.register_error('myskip', lambda e: ('',e.start + 1))
for dirname, dirnames, filenames in os.walk('./'):
    # print path to all filenames.
    if '.git' not in dirname:
        for filename in filenames:
            f = codecs.open(os.path.join(dirname, filename), 'r', 'utf-8', errors = 'myskip')
            content = f.read()
            lines = []
            for line in content.splitlines():
                print line
                #line = line.replace('\xc2\xa0',' ')
                if '\xe2\x80\x99' in line:
                    print 'found stupid utf-8 quote in %s'%filename
                    exit()
                #line = line.replace('\xe2\x80\x99','')
                lines.append(line)

            f.close()
            f = open(os.path.join(dirname, filename), 'w')
            f.write('\n'.join(lines))
            f
