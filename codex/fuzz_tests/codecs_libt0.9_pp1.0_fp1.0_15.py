import codecs
codecs.register(lambda name: codecs.lookup("utf-8") if name == "cp65001" else None)
###least square approximation###
def ls(data):
    x = list(data.keys())
    y = list(data.values())
    xm = mean(x)
    ym = mean(y)
    a = sum(i[0] * i[1] for i in zip(x, y)) / sum(square(n) for n in x)
    b = ym - (a * xm)
    return a, b
### creating adjacency list for graph ###
def create_dict(data):
    a = {}
    for i in data:
        a[int(i[0])] = a.get(int(i[0]), []) + [int(i[1])]
        a[int(i[1])] = a.get(int(i[1]), []) + [int(i[0])]
    return a
### creating adjacency list with values (node#, edge weights) ###
def change_dict
