import threading
threading.stack_size(67108864)

##Run the Thread using Interface
def RunInterface(master,stop_event):

    ##Threading doesn't work without this line
    if stop_event.isSet(): #Run the thread until stop_event is true
        return

    ##Variables
    width = 401
    height = 301
    white = (255,255,255)
    black = (0,0,0)
    box = width/2 
    
    ##Functions

    ##Draw the Game Map
    def map():
        for row in range(0,width,box):
            for y in range(0,height,box):
                a = row
                b = y
                c = a + box
                d = b + box
                img = PIL.ImageDraw.Draw(game_map)
                img.rectangle((a,b,c,d),(255,255,255))

    ##Draw the Game Map
    def player_map():
        for row in range(0,width,box):
            for y in range(0,height,box):
