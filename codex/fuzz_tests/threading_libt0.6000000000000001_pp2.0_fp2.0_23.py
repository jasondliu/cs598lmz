import threading
threading.stack_size(2*1024*1024) # 2MB stack
sys.setrecursionlimit(2**20)  # approx 1 million recursions

def do_floodfill(x,y,old_color,new_color):
    if x < 0 or x > 19:
        return
    if y < 0 or y > 19:
        return
    if grid[y][x] != old_color:
        return
    grid[y][x] = new_color
    do_floodfill(x+1,y,old_color,new_color)
    do_floodfill(x-1,y,old_color,new_color)
    do_floodfill(x,y+1,old_color,new_color)
    do_floodfill(x,y-1,old_color,new_color)

def floodfill(x,y,new_color):
    old_color = grid[y][x]
    do_floodfill(x,y,old_color,new_color)

def print_grid():
   
