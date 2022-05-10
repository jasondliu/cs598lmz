import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class Button(Bg):

    def __init__(self, bg_id=0, bg_priority=0, tile_base=0, palette_id=0,
                 x=0, y=0, width=1, height=1, map_base=0, button_id=0,
                 button_flags=0, callback=None,
                 tile_data=None, map_data=None, palette_data=None,
                 palette_flags=0, priority=0, blend_control=0,
                 window_control=None, shadow=None, overlap=None,
                 bg_size=0):
        Bg.__init__(self, bg_id, bg_priority, tile_base, palette_id,
                    x, y, width, height, map_base, tile_data,
                    map_data, palette_data, palette_flags, priority,
                    blend_control, window_control, shadow, overlap,
                    bg_size)
        self.button_id = button_id
        self.button_flags = button_
