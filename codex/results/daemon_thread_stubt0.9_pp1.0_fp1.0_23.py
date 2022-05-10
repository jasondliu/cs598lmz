import sys, threading

def run():
    c = urllib.request.urlopen(path_list[0])
    
    detabbed_list = list()
    lines_list = list()
    for line in c.readlines():
        lines_list.append(line.decode('utf-8'))

    detabbed_list = detab(lines_list)
    
    
    
    
    
    c.close()

def detab(lines):
    global recols
    detabs = [((i - 40) % recols) + 8 for i, ln in enumerate(lines) if ln.startswith('<a')]
    gaps_list = list()
    for n in detabs:
        for i in range(n, len(lines), recols):
            lines[i] = lines[i].replace('\t', '', 1)
            spaces = 8 - (len(lines[i]) % 8)
            lines[i] = lines[i].replace(' ', spaces*' ', 1)
            gaps_list.append(lines[i].index('  '))
