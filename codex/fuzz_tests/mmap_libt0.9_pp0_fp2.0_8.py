import mmap
import sys

def solve(rows, cols, min_ing, max_cells):
    return "IMPOSSIBLE"

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as fp:
        infile = mmap.mmap(fp.filpno(), 0, prot=mmap.PROT_READ)
        cases = int(infile.readline())
        for i in range(cases):
            lines = infile.readline()
            rows, cols, min_ing, max_cells = lines.split()
            case = infile.readlines()
        # [print x for x in case]
            output = solve(rows, cols, min_ing, max_cells)
            print "Case #{}: {}".format(i + 1, output)
