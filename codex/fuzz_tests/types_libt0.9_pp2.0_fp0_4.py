import types
types.StringTypes

if len(sys.argv)<2:
    print "Usage: python %s <input data file> <radius> <record out file> <analyse file>"%sys.argv[0]
    exit(1)

in_f = open(sys.argv[1],'r')
is_number = lambda x: isinstance(x, (int, long, float, complex))
radius = float(sys.argv[2])
print "Using radius %lf"%radius
rec_f = open(sys.argv[3],'w')
analyse_f = open(sys.argv[4],'w')

def N_radius(point):
    # find centroid point
    xmin=point[0]
    xmax=point[0]
    ymin=point[1]
    ymax=point[1]
    for p in point:
        if p[0]<xmin: xmin=p[0]
        if p[0]>xmax: xmax=p[0]
        if p[1]
