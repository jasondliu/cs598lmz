import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

import pygame

def resize(window, event):
    """
    Resize the viewport.

    :Parameters:
        `window` : Window
            The window that received the resize event.
        `event` : Event
            The pygame event.
    """
    window.clear()
    window.dispatch_event('on_resize', window.width, window.height)
    window.dispatch_event('on_draw')
    window.flip()

def flip(window, event):
    window.flip()

def before_load_image(graphics, image):
    """
    Set the colorkey of PyGame images to be the same as images currently in
    the image cache.
    """
    # TODO: UGH! Workaround for some drivers.
    new_colorkey = None
    for name, img in graphics._image_cache.iteritems():
        if img.get_flags() & pygame.SRCALPHA:
            if new_colorkey is None:
                new_colorkey = img.get_colorkey
