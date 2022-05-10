import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("OpenRoads")

os.system('cls') 

tile = []
for x in range(38):
    tile.append([' '])
    for y in range(25):
        tile[x].append(' ')

tiles = []
for x in range(38):
    tiles.append(['.'])
    for y in range(25):
        tiles[x].append('.')

road = []
for x in range(38):
    road.append([' '])
    for y in range(25):
        road[x].append(' ')

roads = []
for x in range(38):
    roads.append(['.'])
    for y in range(25):
        roads[x].append('.')

tree = []
for x in range(38):
    tree.append([' '])
    for y in range(25):
        tree[x].append(' ')

trees = []
for x in range(38):
    trees.append(['.'])

