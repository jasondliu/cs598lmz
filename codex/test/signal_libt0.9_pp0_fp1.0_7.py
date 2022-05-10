import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)  # Soft Keyboard Interrupt

# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y) # Set POSITION of SDL WINDOW
#
# os.environ['SDL_VIDEO_CENTERED'] = "1"  # center the SDL window on the screen



#Import Icon
# icon = pygame.image.load(os.path.join(
#     os.path.split(sys.path[0])[0], 'include', 'img', 'icon', 'icon4.png'))
# pygame.display.set_icon(icon)


# ==========================
# ==== PYGAME SETTINGS ====
# ==========================
pygame.init()
screen_info = pygame.display.Info()
clock    = pygame.time.Clock()

#Retard of the pygame.gfxdraw.aacircle (how much time we wait before doing a request to the server again, in seconds)

