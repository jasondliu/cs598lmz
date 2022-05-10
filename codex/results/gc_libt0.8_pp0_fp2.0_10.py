import gc, weakref
        
    post_fix = {
        gc.DEBUG_STATS: 'stats',
        gc.DEBUG_LEAK: 'leak',
        0: 'off',
    }
        
    def set_debug_mode(self, debug_flags):
        if self.debug_flags == debug_flags:
            return
        self.debug_flags = debug_flags

        if debug_flags & gc.DEBUG_LEAK:
            self.leak_track = weakref.WeakKeyDictionary()
        else:
            self.leak_track = False
            
        self.update_debug_mode()

    def update_debug_mode(self):
        self.set_debug(self.debug_flags)
            
    def set_debug(self, flags):    
        gc.set_debug(flags)
        if flags & gc.DEBUG_STATS:
            gc.set_threshold(*gc.get_threshold())

    def debug_check_leak(self, obj):
        if self.leak_track is False:

