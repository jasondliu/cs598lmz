import ctypes
FUNTYPE = ctypes.CFUNCTYPE(appuifw.app.body.set_pos)

def update_position(pos):
    appuifw.app.body.set_pos(pos)

update = FUNTYPE(update_position)
observer_token=si.observe_position(update,0.2,0)

"""
Getting the current view (MapWidget)
"""

current_view=p.current_view()


"""
How to get properties of the current view(MapWidget)
"""

"""
scale : current scale of the map
cur_top_left : current top left corner of the map
cur_bottom_right : current bottom right corner of the map

top_left : maximum top left corner
bottom_right : maximum bottom right corner

top_left_tile : top left corner tile indexes
bottom_right_tile : bottom right corner tile indexes
center_tile : center of the map tile indexes

center_lat : lat of the center
center_lon : lon of the center

cur_lat : lat of the top left corner
cur_lon : lon of the top left corner

