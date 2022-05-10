import threading
threading.stack_size(67108864)

import os

def process_one(file_path, fout):
    # print(file_path)
    print(fout.name)
    with open(file_path, 'r') as fp:
        lines = fp.readlines()
        for ln in lines:
            if ln.startswith('#'):
                continue
            if ln.strip() == '':
                continue
            ln = ln.split('#')[0]
            ln = ln.strip()
            if ln[0] == '"' and ln[-1] == '"':
                ln = ln[1:-1]
            ln = ln.lower()
            fout.write(ln)
            fout.write('\n')


def process_file(file_path):
    fout_path = file_path + '.out'
    if os.path.exists(fout_path):
        print('{} already exists, skip'.format(fout_path
